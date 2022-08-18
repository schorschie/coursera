# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, m, M, operators):

    minim = float('inf')
    maxim = float('-inf')

    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        minim = min([minim, a, b, c, d])
        maxim = max([maxim, a, b, c, d])

    return minim, maxim

def get_maximum_value(dataset):
    n = (len(dataset) + 1) // 2
    operators = [dataset[i] for i in  range(1, len(dataset), 2)]

    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        m[i][i] = int(dataset[i*2])
        M[i][i] = int(dataset[i*2])

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, operators)

    return M[0][-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
