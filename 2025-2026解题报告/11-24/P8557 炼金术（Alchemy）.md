# 炼金术

[题目链接](https://www.luogu.com.cn/problem/P8557)

当我们需要炼一类金属时, 我们需要的可能用了一个炉子, 我们也可能用了两个炉子 $\cdots$ 我们可能用了 $k$ 个炉子. 故方案数为

$$
\sum\limits_{i=1}^k\binom{k}{i}=2^k-1
$$

要炼 $n$ 种金属, 故方案数为 $\left(2^k-1\right)^n$.

```cpp
#include<iostream>
#define P(A) A=-~A
typedef long long LL;
const int mod=998244353;
inline LL quick_mod(LL a,LL b){
	LL ans(1);
	for(;b;b>>=1,a=a*a%mod)
		if(b&1)ans=ans*a%mod;
	return ans;
}
signed main(){
	std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
	std::cout.tie(nullptr);
	LL n,k;
	std::cin>>n>>k;
	std::cout<<quick_mod(quick_mod(2,k)-1,n);
	return 0;
}
```
