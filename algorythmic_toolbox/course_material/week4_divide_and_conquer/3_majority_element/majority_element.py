# Uses python3
import sys
#from time import time
#import numpy as np


# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1

#def get_majority_element(a):
#    lena = len(a)
#    mid = [int(lena/2), int(lena/2)+1]
#
#    ascending = sorted(a)
#    descending = sorted(a, reverse=True)
#
#    return any([ascending[m] == descending[m] for m in mid])

def get_majority_element(a):

    n = len(a)
    d = {}

    for b in a:
        d[b] = 0
    for b in a:
        d[b] += 1

    return max(d.values()) > n/2



if __name__ == '__main__':
    DEBUG = not True
    
    if DEBUG:
        a = [2, 3, 9, 2, 2]
        #a = [1, 2, 3, 4]
        #a = [1 ,2, 3, 1]
        #a = np.random.randint(1, 1000, size=50000)
        #n = len(a) -1
    else:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))

    #t = time()
    me = get_majority_element(a)
    if me:
        print(1)
    else:
        print(0)
    #print(time() - t)

