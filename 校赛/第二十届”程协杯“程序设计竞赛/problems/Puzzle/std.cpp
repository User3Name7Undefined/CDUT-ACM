#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define pb push_back
#define ff first
#define ss second
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = 2e6 + 5;
const int M = 1e5 + 5;  
ll mod = 998244353;
ll INF = 1e9;
vector<ll> f(N + 1), invf(N + 1);

ll qpow(ll a, ll b) {
    ll ret = 1;
    a = (a + mod) % mod;
    while (b) {
        if (b & 1) {
            ret = (ret * a) % mod;
        }
        b >>= 1;
        a = (a * a) % mod;
    }
    return ret;
}

ll inv(ll a) {
    return qpow(a, mod - 2);
}

ll C(ll n, ll m) {
    return n >= m ? ((f[n] * invf[m]) % mod * invf[n - m]) % mod : 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    f[0] = 1;
    for (int i = 1; i <= N; ++i) {
        f[i] = (f[i - 1] * i) % mod;
    }
    invf[N] = inv(f[N]);
    for (int i = N - 1; i >= 0; --i) {
        invf[i] = (invf[i + 1] * (i + 1)) % mod;
    }
    int t = 1;
    cin >> t;
    while (t--) {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        ll ans = 0;
        if (abs(a - b) > 1) {
            
        }
        else if (a == 0 && b == 0) {
            if (c && d) {

            }
            else {
                ans = 1;
            }
        }
        else if (a == b) {
            ll x = a + 1, y = a;
            ans = (ans + (C(c + x - 1, x - 1) * C(d + y - 1, y - 1)) % mod) % mod;
            swap(x, y);
            ans = (ans + (C(c + x - 1, x - 1) * C(d + y - 1, y - 1)) % mod) % mod;
        }
        else if (a > b) {
            ll x = a, y = a;
            ans = (ans + (C(c + x - 1, x - 1) * C(d + y - 1, y - 1)) % mod) % mod;            
        }
        else {
            ll x = b, y = b;
            ans = (ans + (C(c + x - 1, x - 1) * C(d + y - 1, y - 1)) % mod) % mod;    
        }
        cout << ans << endl;
    }
    
    return 0;
}