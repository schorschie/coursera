#include <iostream>

int get_change(int m) {
  //write your code here
  int n = 0;
  int coins [3] = {10, 5, 1};

  while (m > 0) {
    if (m >= coins[0]) {
      m = m - coins[0];
      n++;
    } else {
      if ( m >= coins[1]) {
        m = m - coins[1];
        n++;
      } else {
        m = m - coins[2];
        n++;
      }
    } 
  }

  return n;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
