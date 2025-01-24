import random

pisteet = float(input('Syötä pisteiden määrä: '))
N = n = 0
r = 1

while pisteet!=N:
    N+=1
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if (x**2 + y**2) < r:
        n+=1

print(f'Piin likiarvo on {4*n/N}')