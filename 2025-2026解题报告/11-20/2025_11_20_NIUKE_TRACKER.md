# 2025_11_20_NIUKE_TRACKER
哎wc这道题太坏了暴力又过不了  
讨厌这种暴力过不了的题  
题目链接：https://www.nowcoder.com/practice/16d153d47b334b0f8cc507b70a2e2473?channelPut=tracker2
## 神秘预处理
很明显这道题直接枚举是过不了的，我们要对数据进行一些小小的加工。  
为了得到能算出来 gcd 是 $x$ 的子集，这个子集中的所有元素必然都是 $x$ 的倍数。  
而题目又给这个集合中的元素限制了范围：$\forall a\in\mathbb{N}，a<n$（太对了第一次做没看到这句话一直不知道怎么预处理），我们可以把小于 $n$ 的所有 $x$ 的倍数都枚举一遍看他们是否存在，然后对所有 $x$ 的倍数求 gcd 。<br>
### 对于这一坨的gcd一共有三种情况:  

1. 为 $0$ ，也就是说没有 $x$ 的倍数，这个时候输出 `NO`

2. 为 $x$ ，这个时候可以输出 `YES`

3. 为 $x\*n$ 因为这时所有x的倍数的数组成的集合的子集，其 gcd 必然大于等于 $x\*n$ 故不存在子集使得其 gcd 是 $x$ ，输出 `NO`

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
