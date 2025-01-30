import random

tahkot = int(input('Montako sivua nopassa on: '))

def heitto(t):
    noppa = random.randint(1,t)
    return noppa

noppa = heitto(tahkot)
print(noppa)

while noppa!=tahkot:
    noppa = heitto(tahkot)
    print(noppa)