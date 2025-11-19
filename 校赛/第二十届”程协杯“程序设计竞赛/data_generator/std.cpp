#include <iostream>

int main () {
    int t = 1;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        std::cout << bool(n - 1) << '\n';
    }
    return 0;
}
