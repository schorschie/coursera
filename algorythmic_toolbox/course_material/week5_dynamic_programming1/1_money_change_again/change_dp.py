# Uses python3
import sys

def get_change(m):
    coins = [1, 3, 4]
    MinNumCoins = [0] * (m+1)
    
    for ii in range(1, m+1):
        MinNumCoins[ii] = float('inf')
        for kk in range(len(coins)):
            if ii >= coins[kk]:
                NumCoins = MinNumCoins[ii - coins[kk]] + 1
                if NumCoins < MinNumCoins[ii]:
                    MinNumCoins[ii] = NumCoins

    return MinNumCoins[-1]

if __name__ == '__main__':
    DEBUG = not True
    
    if not DEBUG:
        m = int(sys.stdin.read())
    else:
        m = 2
        m = 34
        m = 9
        
    print(get_change(m))
