from cyaron import *
import subprocess
from pathlib import Path
import shutil
import importlib.util
import inspect
import argparse
import re


def load_problem_module(base: Path, problem_name: str):
    """Load a python file named <problem_name>.py from base/generate or base directory as a module.

    Tries `base/generate/<problem_name>.py` first for the new layout, then falls back to
    `base/<problem_name>.py` for backward compatibility.
    """
    gen_dir = base / 'generate'
    candidates = [gen_dir / f"{problem_name}.py", base / f"{problem_name}.py"]
    for mod_path in candidates:
        if mod_path.exists():
            spec = importlib.util.spec_from_file_location(problem_name, str(mod_path))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    # If none found, raise with helpful message listing checked paths
    checked = ', '.join(str(p) for p in candidates)
    raise FileNotFoundError(f'找不到生成器文件 (已检查): {checked}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='数据生成器分发器：调用同目录下的 <problem_name>.py 生成测试')
    parser.add_argument('problem_name', help='问题名称，对应同目录下的 <problem_name>.py')
    parser.add_argument('-c', '--count', type=int, default=20, help='生成测试文件数量（默认 20）')
    parser.add_argument('--tokens', type=str, default=None,
                        help='逗号分隔的要统计的 token 列表，例如 "YES,NO"；不提供则不进行统计')
    parser.add_argument('--ignore-case', action='store_true',
                        help='统计时忽略大小写')
    args = parser.parse_args()

    problem_name = args.problem_name
    count = args.count

    base = Path(__file__).resolve().parent
    # 选择 std 可执行路径（保留原行为）
    std_path = base / 'std.exe'
    if not std_path.exists():
        std_path = base / 'std'

    try:
        module = load_problem_module(base, problem_name)
    except Exception as e:
        print('加载生成器模块失败：', e)
        raise

    if not hasattr(module, 'generate'):
        raise AttributeError(f"模块 {problem_name}.py 必须导出函数 generate(io, data_id) 或 generate(io)")

    gen = module.generate

    for id in range(1, count + 1):
        io = IO(file_prefix=str(base / 'test'), data_id=id)
        # 调用生成器：尽量支持签名 (io, id) 或 (io)
        try:
            sig = inspect.signature(gen)
            params = len(sig.parameters)
        except Exception:
            params = 2

        try:
            if params >= 2:
                gen(io, id)
            elif params == 1:
                gen(io)
            else:
                gen()
        except TypeError:
            # 回退直接尝试 io,id
            gen(io, id)

        # 使用可执行文件的完整路径，避免依赖当前工作目录
        io.output_gen(str(std_path))
        io.close()

        out_path = base / f"test{ id }.out"
        total_lines = 0

        # 如果用户提供了 --tokens，则进行统计；否则跳过统计
        if args.tokens:
            tokens = [t.strip() for t in args.tokens.split(',') if t.strip()]
            counts = {t: 0 for t in tokens}
            if out_path.exists():
                flags = re.IGNORECASE if args.ignore_case else 0
                regexes = {t: re.compile(r"\b" + re.escape(t) + r"\b", flags) for t in tokens}
                try:
                    with out_path.open('r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            total_lines += 1
                            for t, rx in regexes.items():
                                matches = rx.findall(line)
                                if matches:
                                    counts[t] += len(matches)
                except Exception as e:
                    print('读取输出文件进行统计时出错：', out_path.name, e)

            print(f'Generated test{id}.in and test{id}.out')
            if out_path.exists():
                summary = ', '.join(f"{t}={counts[t]}" for t in tokens)
                print(f' -> {out_path.name}: lines={total_lines}, {summary}')
            else:
                print(f' -> {out_path.name} not found, skipped token count')
        else:
            print(f'Generated test{id}.in and test{id}.out')
            print(' -> token counting skipped (no --tokens provided)')

    # 如果存在 sample*.in，则先用 std 执行这些样例，生成 sample*.out（方便本地查看）
    sample_ins = sorted(base.glob('sample*.in'))
    if sample_ins:
        if not std_path.exists():
            print('未找到 std 可执行文件，无法处理 sample*.in；请确保 std.exe 或 std 在同目录或 PATH 中。')
        else:
            for sin in sample_ins:
                sout = sin.with_suffix('.out')
                try:
                    print(f'运行样例 {sin.name} -> {sout.name} ...')
                    with sin.open('rb') as fin, sout.open('wb') as fout:
                        subprocess.run([str(std_path)], stdin=fin, stdout=fout, cwd=str(base))
                        # 已生成样例输出文件：保留以便人工查看
                except Exception as e:
                    print('运行样例出错：', sin.name, e)

    # 所有测试生成完毕后，打包并清理一次
    zip_name = f"{problem_name}.zip"
    out_path = base / zip_name

    seven = shutil.which('7z')
    if not seven:
        print('未找到 7z 可执行程序，跳过打包与自动清理（如需打包请安装 7-Zip 并将 7z.exe 加入 PATH）。')
    else:
        try:
            # 仅打包 test*.in/test*.out，先删除已存在的压缩包以确保重新生成（避免旧条目残留）
            print(f'正在用 7z 打包 {base} 下的 test*.in/test*.out 到 {out_path.name} ...')
            if out_path.exists():
                try:
                    out_path.unlink()
                except Exception as e:
                    print('无法删除已有的压缩文件，仍将尝试覆盖：', out_path, e)
            res = subprocess.run([seven, 'a', '-y', '-tzip', str(out_path), 'test*.in', 'test*.out'], cwd=str(base))
            if res.returncode == 0:
                print('测试集打包完成：', out_path.name)
            else:
                print('7z 打包测试集返回非零状态码：', res.returncode)

            # 打包完成后，删除 test*.in 和 test*.out 保留 sample 文件
            removed = 0
            for p in sorted(base.glob('test*.in')) + sorted(base.glob('test*.out')):
                try:
                    p.unlink()
                    removed += 1
                except Exception as e:
                    print('删除文件失败：', p.name, e)
            print(f'已删除 {removed} 个 test 文件，保留 sample 文件以便观察。')

        except Exception as e:
            print('执行 7z 或清理时发生异常：', e)