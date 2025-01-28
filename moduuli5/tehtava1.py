import random

heitto = int(input('Anna arpakuutioiden lukumäärä: '))
arpakuutiot = []
summa = 0

for arpa in range(heitto):
    luku = random.randint(1,6)
    arpakuutiot.append(luku)
    summa += luku

teksti = '\nHeitit'
for arpa in range(0,heitto):
    if arpa+2 == len(arpakuutiot):  #jos luku on toiseksi viimeinen
        teksti += f' {arpakuutiot[arpa]} ja'
    elif arpa+1 == len(arpakuutiot):    #jos luku on viimeinen
        teksti += f' {arpakuutiot[arpa]}'
    else:
        teksti += f' {arpakuutiot[arpa]},'

print(teksti + f'\nSilmälukujen summa on {summa}')