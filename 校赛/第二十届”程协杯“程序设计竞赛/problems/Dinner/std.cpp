#include<bits/stdc++.h>
#define endl '\n'
#define pii pair<int,int>
#define int long long
using namespace std;

const int N=1e5+10;

int n,r;
int a[N];
vector<pii>to[N];
int ans=0;

void dfs(int u,int fa,int len){
    ans+=a[u]*len;
    for(auto [v,w]:to[u]){
        if(v==fa) continue;
        dfs(v,u,len+w);
    }
}

void solve(int turn){
    cin>>n>>r;
    for(int i=1;i<=n;i++) to[i].clear();
    for(int i=1;i<n;i++){
        int u,v,w; cin>>u>>v>>w;
        to[u].push_back({v,w});
        to[v].push_back({u,w});
    }
    for(int i=1;i<=n;i++) cin>>a[i];
    ans=0;
    dfs(r,0,0);
    cout<<ans<<endl;
}

signed main(void){
    ios::sync_with_stdio(false),cin.tie(nullptr),cout.tie(nullptr);
    int T=1; cin>>T;
    for(int i=1;i<=T;i++){
        solve(i);
    }
    return 0;
}