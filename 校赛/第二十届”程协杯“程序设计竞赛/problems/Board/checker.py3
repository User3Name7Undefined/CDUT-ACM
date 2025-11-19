std_input = open("input")
user_output = open("user_output")

T = int(std_input.readline())
for _ in range(T):
    n, m, x = map(int, std_input.readline().split())

    BB = []

    for _ in range(n):
        A = map(int,std_input.readline().split())
        B = map(int,user_output.readline().split())

        line=[]
        for a,b in zip(A,B):
            if b != a and b != a + x:   #判断B_ij是否为A_ij或A_ij + x
                exit(1)
            line.append(b)
            
        BB.append(line)  #加入B矩阵

    for i in range(n):
        for j in range(m):
            if i > 0:
                if BB[i][j] == BB[i-1][j]:    #判断是否与上方相等
                    exit(1)
            if j > 0:
                if BB[i][j] == BB[i][j-1]:    #判断是否与左方相等
                    exit(1)

std_input.close()
user_output.close()
exit(0) #全部通过