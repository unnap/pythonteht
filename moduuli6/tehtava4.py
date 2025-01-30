import random

def listan_summa(l):
    summa = 0
    for i in l:
        summa += i
    return summa

lista = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(f'Listan {lista} summa on {listan_summa(lista)}')