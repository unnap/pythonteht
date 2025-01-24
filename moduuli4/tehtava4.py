import random

numero = random.randint(1,10)
#print(numero)
arvaus = int(input('Arvaa numero 1 ja 10 väliltä: '))

while arvaus!=numero:
    if arvaus<numero:
        print('Liian pieni arvaus')
    elif arvaus>numero:
        print('Liian suuri arvaus')
    arvaus = int(input('Arvaa numero 1 ja 10 väliltä: '))
print('Oikein!')