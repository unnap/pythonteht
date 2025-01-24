luku = input('Anna luku: ')
pLuku = sLuku = float(luku)

while luku!='':
    if float(luku)<pLuku:
        pLuku = float(luku)
    if float(luku)>sLuku:
        sLuku = float(luku)
    luku = input('Anna luku: ')
print(f'\nPienin annettu luku: {pLuku}\n'
      f'Suurin annettu luku: {sLuku}')


#Ratkaisuni ennen kuin kysyin miten tämä tehdään ilman listaa
"""
luvut = []
while luku!='':
    luvut.append(float(luku))
    luku = input('Anna luku: ')
print(f'\nPienin annettu luku: {min(luvut)}\n'
      f'Suurin annettu luku: {max(luvut)}')
"""