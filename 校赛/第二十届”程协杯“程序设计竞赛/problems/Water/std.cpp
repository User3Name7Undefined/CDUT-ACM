#include<bits/stdc++.h>
#define endl '\n'
#define pii pair<int,int>
using namespace std;

const int N=50;


int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

int n,m,k;
int f[N][N];

bool out(int x,int y){
    return x<0||x>=n||y<0||y>=m;
}

bool round5(int x,int y){
    int cnt=0;
    for(int i=0;i<4;++i){
        int nx=x+dx[i],ny=y+dy[i];
        if(out(nx,ny)) continue;
        if(f[nx][ny]==5) ++cnt;
    }
    return cnt>=2;
}

void solve(){
    cin>>n>>m>>k;
    queue<pii>q;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            f[i][j]=0;
        }
    }
    
    //先处理水源
    for(int i=1;i<=k;++i){
        int x,y; cin>>x>>y;
        f[x][y]=5;
        q.push({x,y});
    }
    while(!q.empty()){
        auto [x,y]=q.front(); q.pop();
        for(int i=0;i<4;++i){
            int nx=x+dx[i],ny=y+dy[i];
            if(out(nx,ny)) continue;

            if(f[nx][ny]==5)continue;
            if(round5(nx,ny)){
                f[nx][ny]=5;
                q.push({nx,ny});
            }
        }
    }

    //普通水流
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            if(f[i][j]==5){
                q.push({i,j});
            }
        }
    }
    while(!q.empty()){
        auto [x,y]=q.front(); q.pop();
        for(int i=0;i<4;++i){
            int nx=x+dx[i],ny=y+dy[i];
            if(out(nx,ny)) continue;
            if(f[nx][ny]>=f[x][y]-1) continue;
            f[nx][ny]=f[x][y]-1;
            q.push({nx,ny});
        }
    }

    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            cout<<f[i][j];
        }
        cout<<endl;
    }
}

signed main(void){
    ios::sync_with_stdio(false),cin.tie(nullptr),cout.tie(nullptr);
    int T=1; cin>>T;
    while(T--)solve();
    return 0;
}