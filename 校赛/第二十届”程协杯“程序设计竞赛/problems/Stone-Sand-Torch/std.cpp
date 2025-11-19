#include<bits/stdc++.h>
#define tiii tuple<int,int,int>
using namespace std;

const int N=11;

int delta[][3]={
    {-1,0,0},
    {1,0,0},
    {0,-1,0},
    {0,1,0},
    {0,0,-1},
    {0,0,1},
};

struct C3{
    int x,y,z;
};

int X,Y,Z;
int n;

int world[N][N][N];
/*
-1 air
0 torch -1,0,0 ^
1 torch 1,0,0 v
2 torch 0,-1,0 <
3 torch 0,1,0 >
4 torch 0,0,-1 t
5 stone
6 sand
*/

bool Inside(int x,int y,int z=0){
    if(x<0||x>=X||y<0||y>=Y||z<0||z>=Z)return false;
    return true;
}

bool state[N][N][N];
/*
0 stable
1 falls or disappear
*/

tiii get_target(int x,int y,int z,int f){
    int tx=x+delta[f][0];
    int ty=y+delta[f][1];
    int tz=z+delta[f][2];
    return make_tuple(tx,ty,tz);
}

bool CanStay(int x,int y,int z,bool type){//0 torch;1 other
    if(z==-1)return true;
    if(!Inside(x,y,z))return false;
    if(state[x][y][z])return false;
    if(!type){ //torch
        return (world[x][y][z]==5||world[x][y][z]==6);
    }else{ //other
        return (world[x][y][z]!=-1);
    }
    return false;
}

void Update(){
    for(int k=0;k<Z;++k){   //update from bottom
        for(int i=0;i<X;++i){for(int j=0;j<Y;++j){  //sand
            if(world[i][j][k]!=6)continue;
            if(!CanStay(i,j,k-1,1)){
                state[i][j][k]=true;   //update
            }
        }}

        for(int i=0;i<X;++i){for(int j=0;j<Y;++j){  //torch
            if(world[i][j][k]<0||world[i][j][k]>4)continue;
            auto [tx,ty,tz]=get_target(i,j,k,world[i][j][k]);
            if(!CanStay(tx,ty,tz,0)){
                state[i][j][k]=true;   //update
            }
        }}
    }

    for(int i=0;i<X;++i){for(int j=0;j<Y;++j){for(int k=0;k<Z;++k){//remove all torches
        if(world[i][j][k]<0||world[i][j][k]>4)continue;
        if(state[i][j][k]){
            world[i][j][k]=-1;
        }
    }}}

    for(int k=0;k<Z;++k){   //drop all sands
        for(int i=0;i<X;++i){for(int j=0;j<Y;++j){
            if(!state[i][j][k])continue;
            if(world[i][j][k]!=6)continue;
            //unstable sand drop
            int nowz=k;
            while(nowz!=0&&world[i][j][nowz-1]==-1)--nowz;
            world[i][j][k]=-1;
            world[i][j][nowz]=6;
        }}
    }

    for(int i=0;i<X;++i){for(int j=0;j<Y;++j){for(int k=0;k<Z;++k){
        state[i][j][k]=false;
    }}}
}

char out[]={
    'a','^','v','<','>','t','r','s'
};

void Out(){
    for(int k=0;k<Z;++k){for(int i=0;i<X;++i){for(int j=0;j<Y;++j){
        cout<<out[world[i][j][k]+1];
    }cout<<'\n';}cout<<endl;}
}

void Success(){
    cout<<"GOODJOB"<<endl;
    Update();
}

void Fail(){
    cout<<"AREYOUKIDDINGME"<<endl;
}

void Put(int x,int y,int z,int type){
    if(world[x][y][z]!=-1){
        Fail();
        return;
    }

    for(int f=0;f<6;++f){
        auto [ax,ay,az]=get_target(x,y,z,f);
        if(CanStay(ax,ay,az,1)){    //check if exist block nearby
            world[x][y][z]=type;
            Success();
            return;
        }
    }
    Fail();
    return;
}

void PutTorch(int x,int y,int z,int f){
    if(world[x][y][z]!=-1){
        Fail();
        return;
    }
    switch(f){
        case 1:f=1; break;
        case 2:f=0; break;
        case 3:f=3; break;
        case 4:f=2; break;
        case 5:f=4; break;
    }
    auto [ax,ay,az]=get_target(x,y,z,f);
    if(CanStay(ax,ay,az,0)){ //can attach
        world[x][y][z]=f;
        Success();
        return;
    }
    Fail();
    return;
}

void Destroy(int x,int y,int z){
    if(world[x][y][z]!=-1){
        world[x][y][z]=-1;
        Success();
        return;
    }
    Fail();
    return;
}

void solve(){
    cin>>X>>Y>>Z;
    for(int i=0;i<X;++i){for(int j=0;j<Y;++j){for(int k=0;k<Z;++k){
        world[i][j][k]=-1;
    }}}

    bool flag=false;
    cin>>n;
    while(n--){
        string str; int x,y,z,f;
        cin>>str>>x>>y>>z;
        if(str=="PUT_STONE"){
            Put(x,y,z,5);
        }else if(str=="PUT_SAND"){
            Put(x,y,z,6);
        }else if(str=="PUT_TORCH"){
            cin>>f;
            PutTorch(x,y,z,f);
        }else{
            Destroy(x,y,z);
        }
    }
    Out();
}

signed main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T=1; //cin>>T;
    while(T--)solve();
    return 0;
}