# Uses python3
from logging import captureWarnings
import sys

def get_optimal_value(capacity, weights, values):

    if capacity == 0 or len(weights) == 0:
        return 0
    
    relative_value = [values[idx] / weights[idx] for idx, _ in enumerate(values)]
    m = relative_value.index(max(relative_value))
    
    amount = min([weights[m], capacity])
    value = values[m] * amount / weights[m]

    weights.pop(m)
    values.pop(m)

    return value + get_optimal_value(capacity-amount, weights, values)


if __name__ == "__main__":
    DEBUG = False
    
    if not DEBUG:
        data = list(map(int, sys.stdin.read().split()))
        n, capacity = data[0:2]
        values = data[2:(2 * n + 2):2]
        weights = data[3:(2 * n + 2):2]
    else:
        capacity = 50
        weights = [20, 50, 30]
        values = [60, 100, 120]
        #capacity = 10
        #weights = [30]
        #values = [500]

        
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
