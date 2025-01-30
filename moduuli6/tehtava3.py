muunnos = 3.785

def litrat(g):
    l = g*muunnos
    return l

gallonat = float(input('Anna gallonat: '))

if gallonat<0:
    print('Heippa')

while gallonat>0:
    print(f'{gallonat:.2f} gallonaa on {litrat(gallonat):.2f} litraa')
    gallonat = float(input('Anna gallonat: '))
    if gallonat<0:
        print('Heippa')