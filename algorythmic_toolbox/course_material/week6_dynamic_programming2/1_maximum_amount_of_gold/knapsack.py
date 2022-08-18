# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here

    assert isinstance(W, int), \
        'W must be integer.'
    assert isinstance(w, list) and all([isinstance(x, int) for x in w]), \
        'w must be list of integers.'
    
    w.sort()
    
    optimal_path = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]

    for row in range(1,len(w)+1):
        for col in range(1, W+1):
            if col >= w[row-1]:
                optimal_path[row][col] = max([optimal_path[row-1][col],
                                              optimal_path[row][col-1],
                                              optimal_path[row-1][col-w[row-1]] + w[row-1]])
            else:
                optimal_path[row][col] = max([optimal_path[row-1][col],
                                              optimal_path[row][col-1]])
        
    return optimal_path[-1][-1]

if __name__ == '__main__':
    DEBUG = not True
    if not DEBUG:
        input = sys.stdin.read()
        W, n, *w = list(map(int, input.split()))
    else:
        W = 10
        w = [1, 4, 8]
        W  = 10
        w = [3, 5, 3, 3, 5]
    
    print(optimal_weight(W, w))
