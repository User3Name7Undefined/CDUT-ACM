# 2025_11_20_NIUKE_TRACKER
哎wc这道题太坏了暴力又过不了<br>
讨厌这种暴力过不了的题<br>
题目链接：https://www.nowcoder.com/practice/16d153d47b334b0f8cc507b70a2e2473?channelPut=tracker2
## 神秘预处理
很明显这道题直接枚举是过不了的，我们要对数据进行一些小小的加工。<br>
为了得到能算出来gcd是x的子集，这个子集中的所有元素必然都是x的倍数。<br>
而题目又给这个集合中的元素<span style="color: red;">限制了范围：∀a ∈N，a<n</span>（太对了第一次做没看到这句话一直不知道怎么预处理），我们可以把小于n的所有x的倍数都枚举一遍看他们是否存在，然后对所有x的倍数求gcd。<br>
### 对于这一坨的gcd一共有三种情况:  
1. 为0，也就是说没有x的倍数，这个时候输出NO

2. 为x，这个时候可以输出YES

3. 为 $$x*n$$ 因为这时所有x的倍数的数组成的集合的子集，其gcd必然大于等于 $$x*n$$ 故不存在子集使得其gcd是x，输出NO
## 代码实现
```cpp
//判断单个输入是否满足条件
//其他的懒得弄了
//前面开了一个存这个集合的vector和存元素存在个数的set
int middlenum=0;
int TheGCD=0;
cin>>middlenum;
for(int i=1;i*middlenum<n;i++){
    int num=i*middlenum;
    if(TheSET.count(num)){
            if(!TheGCD)
                TheGCD=middlenum;
            else 
                TheGCD=GCD(TheGCD,num);
    }
    if(TheGCD==middlenum)
        break;
}
if(TheGCD==middlenum)
    cout<<"YES";
else
    cout<<"NO";
//看得懂就行了大概率有错懒得看源码了
