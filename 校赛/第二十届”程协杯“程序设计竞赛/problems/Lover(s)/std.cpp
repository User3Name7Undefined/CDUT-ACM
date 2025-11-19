#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

const int N=1e5+10;

int n,m;
int a[N];
int b[N];

void solve(int turn){
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=m;i++) cin>>b[i];
    int ans=0;
    for(int i=1;i<=n;i++){
        if(b[a[i]]==i){
            ans++;
        }
    }
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