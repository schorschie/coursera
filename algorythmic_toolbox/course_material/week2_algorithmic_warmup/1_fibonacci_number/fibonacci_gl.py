# fibonacci.py
# Calculate fibonacci number

import matplotlib.pyplot as plt

f = lambda n: int ( 5**(-0.5) * ( ( (1 + 5**0.5) / 2)**n - ( (1 - 5**0.5) / 2 )**n ) )

N = 20
x = range(N)
y = [f(n) for n in x]

_, ax = plt.subplots()

ax.stem(x, y)
ax.set_yscale('log')

plt.show()
