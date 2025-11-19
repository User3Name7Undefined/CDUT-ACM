#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define pb push_back
#define ff first
#define ss second
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = 1e5 + 5;
const int M = 1e5 + 5;  
ll mod = 1e9 + 7;
ll INF = 1e9;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    cin >> t;
    while (t--) {
        int n, m, x;
        cin >> n >> m >> x;
        vector<vector<int>> a(n, vector<int>(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> a[i][j];
                int f1 = (a[i][j] / x) % 2;
                int f2 = (i + j) % 2;
                if (f1 != f2) {
                    a[i][j] += x;
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cout << a[i][j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}