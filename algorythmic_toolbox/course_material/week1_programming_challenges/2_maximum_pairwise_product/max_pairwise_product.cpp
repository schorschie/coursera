#include <iostream>
#include <vector>
#include <algorithm>
// #include <ctime>


long long MaxPairwiseProduct(const std::vector<long long>& numbers) {
    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

long long MaxPairwiseProductFast(const std::vector<long long>& numbers) {

    int n = numbers.size();

    int max_index_1 = -1;
    for (int ii = 0; ii < n; ++ii) {
        if ((max_index_1 == -1) || (numbers[ii] > numbers[max_index_1])) {
            max_index_1 = ii;
        }
    }
    
    int max_index_2 = -1;
    for (int ii = 0; ii < n; ii++) {
        if ((ii != max_index_1) && ((max_index_2 == -1) || (numbers[ii] > numbers[max_index_2]))) {
            max_index_2 = ii;
        }
    }

    long long max_product = numbers[max_index_1] * numbers[max_index_2] ;

    return max_product;
}

int main() {
    
    /*
    while (true) {
        int n = rand() % 10000 + 2;
        std::cout << n << "\n";
        std::vector<long long> a;
        
        for (int i=0; i < n; i++) {
            a.push_back(rand() % 10000) ;
        }
        for (int i=0; i < n; i++) {
            std::cout << a[i] << " ";
        }
        std::cout << "\n";

        double start_time = clock() / CLOCKS_PER_SEC ;
        long long result_1 = MaxPairwiseProduct(a);
        long long result_2 = MaxPairwiseProductFast(a);
        double time_delta = start_time - clock() / CLOCKS_PER_SEC ;

        if (result_1 != result_2) {
            std::cout << "Wrong answer: " << result_1 << " " << result_2 << "\n";
            break;
        } else {
            std::cout << "OK.\n";
        }   
        std::cout << "Runtime: " << time_delta << "\n";
    }
    */

    int n;
    std::cin >> n;
    std::vector<long long> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    long long result = MaxPairwiseProductFast(numbers);
    // long long result = MaxPairwiseProductFast(numbers);
    std::cout << result << "\n";

    return 0;
}
