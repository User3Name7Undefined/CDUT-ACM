#include<bits/stdc++.h>
#define endl '\n'
#define int long long
using namespace std;

const int N=2e5+10;

int n;
int a[N];

void solve(int turn){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    sort(a+1,a+n+1);
    int ans=0;
    int now=0;
    for(int i=1;i<=n;i++){
        now+=a[i];
        ans+=now;
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