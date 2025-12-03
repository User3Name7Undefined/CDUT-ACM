[[USACO20JAN] Wormhole Sort S](https://www.luogu.com.cn/problem/P6004)

目前为止遇到最简单的题目.

显然我们优先枚举大的, 每枚举一次进行一次判断. 显然时间复杂度是 $O\left(nm\alpha(n)\right)$. 故我们考虑对 $w$ 进行二分. 每二分一次就合并, 判断一起上. 时间复杂度预计 $O\left((n+m)\alpha(n)\log w_{max}\right)$.

代码:

```cpp
#include<iostream>
#include<algorithm>
#include<cstdlib>
#define P(A) A=-~A
typedef long long LL;
#define NUMBER1 100000
int position[NUMBER1+5],f[NUMBER1+5],n,m;
struct Wormhole{
	int a,b,w;
	bool operator<(const Wormhole &A)const{return w>A.w;}
}hole[NUMBER1+5];
inline int find(int x){return x==f[x]?x:f[x]=find(f[x]);}
inline bool check(int w){
	for(int i=1;i<=n;P(i))f[i]=i;
	for(int i=1,x,y;i<=m&&hole[i].w>=w;P(i)){
		x=find(hole[i].a),y=find(hole[i].b);
		if(x^y)f[x]=y;
	}
	for(int i=1;i<=n;P(i))
		if(find(i)^find(f[position[i]]))return false;
	return true;
}
signed main(){
	std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
	std::cout.tie(nullptr);
	std::cin>>n>>m;
	bool need_move(false);
	for(int i=1;i<=n;P(i)){
		std::cin>>position[i];
		if(position[i]^i)need_move=true;
	}
	if(!need_move){
		std::cout<<-1;
		exit(0);
	}
	for(int i=1;i<=m;P(i))std::cin>>hole[i].a>>hole[i].b>>hole[i].w;
	std::sort(hole+1,hole+1+m);
	int l=0,r=hole[1].w,ans;
	for(int mid;l<=r;){
		mid=(l+r)>>1;
		if(check(mid))ans=mid,l=mid+1;
		else r=mid-1;
	}
	std::cout<<ans;
	return 0;
}
```
