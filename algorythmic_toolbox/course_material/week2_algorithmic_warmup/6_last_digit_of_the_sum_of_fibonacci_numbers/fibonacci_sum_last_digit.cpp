#include <iostream>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int get_fibonacci_last_digit_sum_fast(long long n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;
    int sum      = 1;
    int tmp_previous ;

    for (long long i = 0; i < n - 1; ++i) {
        tmp_previous = previous;
        previous = current % 10;
        current = (tmp_previous + current) % 10;
        sum = (sum + current) % 10 ;
    }
    return sum;
}


int main() {
    long long n = 0;
    std::cin >> n;
    //std::cout << fibonacci_sum_naive(n);
    std::cout << get_fibonacci_last_digit_sum_fast(n);
}
