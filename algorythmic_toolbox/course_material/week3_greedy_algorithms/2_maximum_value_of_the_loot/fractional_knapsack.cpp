#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;
  if (capacity == 0 ) {
    return 0.0;
  }

  // write your code here
  int idv = distance(values, max_element(values.begin(), values.end()));
  
  for (auto i: values)
    std::cout << i << ' ';
  std::cout << '\n' << idv ;
  return value;
}

int main() {
  //int n = 3;
  int capacity = 4;
  //std::cin >> n >> capacity;
  vector<int> values = {5000, 200, 10};
  vector<int> weights = {5, 3, 15};
  /*for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }*/

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
