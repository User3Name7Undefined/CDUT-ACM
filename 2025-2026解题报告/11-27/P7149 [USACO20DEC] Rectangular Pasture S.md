[[USACO20DEC] Rectangular Pasture S](https://www.luogu.com.cn/problem/P7149)

显然奶牛坐标最高可达 $1e9$, 所以我们先离散化.

```cpp
for(int i=1;i<=n;P(i)){
	std::cin>>a[i].first>>a[i].second;
	kkk[0].push_back(a[i].first);
	kkk[1].push_back(a[i].second);
}
std::sort(kkk[0].begin(),kkk[0].end());
std::sort(kkk[1].begin(),kkk[1].end());
auto p0=std::unique(kkk[0].begin(),kkk[0].end());
auto p1=std::unique(kkk[1].begin(),kkk[1].end());
kkk[0].erase(p0,kkk[0].end());
kkk[1].erase(p1,kkk[1].end());
for(int i=1;i<=n;P(i)){
	a[i].first=std::lower_bound(kkk[0].begin(),kkk[0].end(),a[i].first)-kkk[0].begin()+1;
	a[i].second=std::lower_bound(kkk[1].begin(),kkk[1].end(),a[i].second)-kkk[1].begin()+1;
	f[a[i].first][a[i].second]=1;
}
```

显然我们的目的是要去枚举子集. 我们不妨先把坐标排序, 枚举矩形的上下界, 再统计矩形左右两边有相同上下界牛的个数, 相乘即可.  
我们以 $y$ 为关键字排序, 这样我们就可以直接枚举 $y\in[i,j]$ 了.

```cpp
std::sort(a+1,a+1+n,[](const PII& A, const PII& B){return A.second<B.second;});
for(int i=1,max,min;i<=n;P(i))
for(int j=i;j<=n;P(j)){
	max=a[i].first,min=a[j].first;
	if(max<min)std::swap(max,min);
	ans+=1ll*(f[n][j]-f[max-1][j]-f[n][i-1]+f[max-1][i-1])*1ll*(f[min][j]-f[0][j]-f[min][i-1]+f[0][i-1]);
}
```

最终答案补上空集即可.

```cpp
ans++;
```

总代码:

```cpp
#include<iostream>
#include<vector>
#include<algorithm>
#define P(A) A=-~A
typedef std::pair<int,int> PII;
typedef long long LL;
#define NUMBER1 2500
int n,f[NUMBER1+5][NUMBER1+5];
PII a[NUMBER1+5];
LL ans(0);
std::vector<int>kkk[2];
signed main(){
	std::cin.tie(nullptr)->std::ios::sync_with_stdio(false);
	std::cout.tie(nullptr);
	std::cin>>n;
	for(int i=1;i<=n;P(i)){
		std::cin>>a[i].first>>a[i].second;
		kkk[0].push_back(a[i].first);
		kkk[1].push_back(a[i].second);
	}
	std::sort(kkk[0].begin(),kkk[0].end());
	std::sort(kkk[1].begin(),kkk[1].end());
	auto p0=std::unique(kkk[0].begin(),kkk[0].end());
	auto p1=std::unique(kkk[1].begin(),kkk[1].end());
	kkk[0].erase(p0,kkk[0].end());
	kkk[1].erase(p1,kkk[1].end());
	for(int i=1;i<=n;P(i)){
		a[i].first=std::lower_bound(kkk[0].begin(),kkk[0].end(),a[i].first)-kkk[0].begin()+1;
		a[i].second=std::lower_bound(kkk[1].begin(),kkk[1].end(),a[i].second)-kkk[1].begin()+1;
		f[a[i].first][a[i].second]=1;
	}
	for(int i=1;i<=n;P(i))
		for(int j=1;j<=n;P(j))
			f[i][j]+=f[i-1][j]+f[i][j-1]-f[i-1][j-1];
	std::sort(a+1,a+1+n,[](const PII& A, const PII& B){return A.second<B.second;});
	for(int i=1,max,min;i<=n;P(i))
		for(int j=i;j<=n;P(j)){
			max=a[i].first,min=a[j].first;
			if(max<min)std::swap(max,min);
			ans+=1ll*(f[n][j]-f[max-1][j]-f[n][i-1]+f[max-1][i-1])*1ll*(f[min][j]-f[0][j]-f[min][i-1]+f[0][i-1]);
		}
	std::cout<<ans+1;
	return 0;
}
```
