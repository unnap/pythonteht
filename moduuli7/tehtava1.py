kuukaudet = ('Tammi','Helmi','Maalis','Huhti',
             'Touko','Kesä','Heinä','Elo','Syys',
             'Loka','Marras','Joulu')
kuu = 'kuussa on '
vuodenajat = ('talvi','kevät','kesä','syksy')
kk = int(input('Kuukauden numero: '))

if kk<=0:
    print('Viallinen numero')
elif kk<=2 or kk==12:
    print(kuukaudet[kk-1]+kuu+vuodenajat[0])
elif kk<=5:
    print(kuukaudet[kk-1]+kuu+vuodenajat[1])
elif kk<=8:
    print(kuukaudet[kk-1]+kuu+vuodenajat[2])
elif kk<=11:
    print(kuukaudet[kk-1]+kuu+vuodenajat[3])
else:
    print('Viallinen numero')