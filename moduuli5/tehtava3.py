luku = int(input('Anna kokonaisluku: '))
testi = False
ei = []

for l in range(2,luku-1):
    if luku%l==0:
        testi = True
        break

if testi == True:
    print(f'{luku} ei ole alkuluku')
else:
    print(f'{luku} on alkuluku')

#Tein toisenkin ratkaisun ihan vain harjoituksen vuoksi
#Jätin aiemman ratkaisun aktiiviseksi kun se on nätimpi
"""
for l in range(2,luku-1):
    if luku%l==0:
        ei.append(l)

if len(ei)==0:
    print(f'{luku} on alkuluku')
else:
    teksti = f'{luku} ei ole alkuluku sillä se on jaollinen luvuilla'
    for l in range(len(ei)):
        teksti += f' {ei[l]}'
    print(teksti)
"""