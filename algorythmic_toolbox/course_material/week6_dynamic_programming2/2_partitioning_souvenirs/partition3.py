# Uses python3
import sys
#import random
import numpy as np

def optimal_weight(W, w):

    assert isinstance(W, int), \
        'W must be integer.'
    assert isinstance(w, list) and all([isinstance(x, int) for x in w]), \
        'w must be list of integers.'
    
    #w.sort()
    #random.shuffle(w)
    
    num_rows = len(w) + 1
    num_cols = W+1
    optimal_path = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if col >= w[row-1]:
                optimal_path[row][col] = max([optimal_path[row-1][col],
                                              optimal_path[row][col-1],
                                              optimal_path[row-1][col-w[row-1]] + w[row-1]])
            else:
                optimal_path[row][col] = max([optimal_path[row-1][col],
                                              optimal_path[row][col-1]])
    
    return optimal_path

# def get_is_partitionable(A):
#     
#     W = sum(A) // 3
#     n = len(A)
#     items = A.copy()
# 
#     count = 0 
#     value = np.zeros((W+1, n+1))
# 
#     for i in range(1, W+1):
#         for j in range(1, n+1):
#             value[i][j] = value[i][j-1]
#             if items[j-1]<=i:
#                 temp = value[i-items[j-1]][j-1] + items[j-1]
#                 if temp > value[i][j]:
#                     value[i][j] = temp
#             if value[i][j] == W:
#                 count += 1
# 
# 
#     if count < 3:
#         return 0
#     else: 
#         return 1
    
def partition3(A):
    if any([a <= 0 for a in A]):
        raise ValueError

    is_partitionable = False
    if sum(A) % 3 == 0 and len(A) >= 3 and sum(A) >= 3:
        a = sum(A) // 3
        op = optimal_weight(a, A)
        
        # For the souvenirs to be partitionable into 3 subsets, there must
        # be at least three sub-knapsacks with the value of a:
        is_partitionable = sum([sum([cell == a for cell in row]) for row in op]) >= 3
        # is_partitionable = get_is_partitionable(A)

    return int(is_partitionable)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    
    print(partition3(A))
