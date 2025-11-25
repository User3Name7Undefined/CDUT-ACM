# [ICPC 2022 Jinan R] Best Carry Player

[题目链接](https://www.luogu.com.cn/problem/P9679)

通过观察, 显然无论怎么调整顺序, 最终进位次数相同. 证明:

无论怎么调整顺序, 个位进位次数相同.  
同理, 无论怎么调整顺序, 十位数进位次数相同 $\cdots$

总之, 无论怎么调整顺序, 最终进位次数相同.

进位代码

```cpp
inline int get_merge(LL a,LL b){
	int cnt(0);
	for(int num(0);a||b;a/=10,b/=10){
		if(a%10+b%10+num>=10)num=1,P(cnt);
		else num=0;
	}
	return cnt;
}
```

总代码

```cpp
#include<iostream>
#define P(A) A=-~A
typedef long long LL;
inline int get_merge(LL a,LL b){
	int cnt(0);
	for(int num(0);a||b;a/=10,b/=10){
		if(a%10+b%10+num>=10)num=1,P(cnt);
		else num=0;
	}
	return cnt;
}
inline void solve(){
	int n;
	LL end,ans(0);
	std::cin>>n>>end;
	for(int i=2,a;i<=n;P(i)){
		std::cin>>a;
		ans+=get_merge(a,end);
		end+=a;
	}
	std::cout<<ans<<'\n';
}
signed main(){
	std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
	std::cout.tie(nullptr);
	int T;
	std::cin>>T;
	while(T--)solve();
	return 0;
}
```
