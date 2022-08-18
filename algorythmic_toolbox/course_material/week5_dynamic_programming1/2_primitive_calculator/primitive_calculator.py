# Uses python3
from distutils.debug import DEBUG
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if (n % 3 == 0):
#             n = n // 3
#         elif (n-1) % 3 == 0:
#             n = n - 1
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def optimal_sequence(n):
    opt_seq = [0] * (n+1)
    
    path = [0] * (n+1)

    for ii in range(1, n+1):

        path_three_cost = float('inf')
        path_two_cost = float('inf')
        path_one_cost = opt_seq[ii-1] + 1  # path one is always possible


        if ii % 2 == 0:
            path_two_cost = opt_seq[ii // 2] + 1

        if ii % 3 == 0:
            path_three_cost = opt_seq[ii // 3] + 1

        path_costs = [path_one_cost, path_two_cost, path_three_cost]
        
        opt_seq[ii] = min(path_costs)
        
        if path_one_cost == min(path_costs):
            path[ii] = 1
        elif path_two_cost == min(path_costs):
            path[ii] = 2
        else:
            path[ii] = 3

    sequence = [n]
    
    while sequence[-1] > 1:
        if path[sequence[-1]] == 1:
            sequence.append(sequence[-1] - 1)
        elif path[sequence[-1]] == 2:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(sequence[-1] // 3)
            
    return reversed(sequence)


DEBUG = not True
if not DEBUG:
    input = sys.stdin.read()
    n = int(input)
else:
    n = 10
    n = 5
    n = 96234
    #n = 12
    #n = 30
    

sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
