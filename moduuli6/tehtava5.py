import random

lista = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]

def parittomat_poies(l):
    i=0
    while i<len(l):
        if l[i]%2!=0:
            l.pop(i)
        else:
            i+=1
    return l

print(f'Lista ennen parittomien karsintaa:\n'
      f'{lista}\n\n'
      f'Lista karsinnan jälkeen:\n'
      f'{parittomat_poies(lista)}')