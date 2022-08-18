#include <iostream>

int EuclidGCD(int a, int b) {
  if (b == 0) {
    return a ;
  }
  int a_prime = a % b ;
  return EuclidGCD(b, a_prime);
}

long long lcm_fast(int a, int b) {
  long long lcm = a / EuclidGCD(a, b) ;
  lcm = lcm * b ;
  return lcm ;
}

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  //std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b) << std::endl;
  return 0;
}
