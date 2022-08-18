#include <iostream>


// Calculate and return Pisano Period
// The length of a Pisano Period for
// a given m ranges from 3 to m * m
// source:
// https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/

long pisano(long m)
{
    long prev = 0;
    long curr = 1;
    long res = 0;
 
    for(int i = 0; i < m * m; i++)
    {
        long temp = 0;
        temp = curr;
        curr = (prev + curr) % m;
        prev = temp;
 
        if (prev == 0 && curr == 1)
            res = i + 1;
    }
    return res;
}

int get_fibonacci_module_fast(long long n, long long m) {
    
    n = n % pisano(m) ;
    if (n <= 1) {
        return n;
    }


    int previous = 0;
    int current  = 1;
    int tmp_previous ;

    for (int i = 0; i < n - 1; ++i) {
        tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % m;
    }
    return current;
}

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    //std::cout << get_fibonacci_huge_naive(n, m) << '\n';
    std::cout << get_fibonacci_module_fast(n, m) << '\n';
}
