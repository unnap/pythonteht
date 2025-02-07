import mysql.connector


kenttiaTxt = 'kenttiä: '

kenttaLista = {'heliport': [0,'Helikopteri'],
               'small_airport': [0,'Pieniä lento'],
               'closed': [0,'Kiinni olevia '],
               'seaplane_base': [0, 'Vesilentokone'],
               'balloonport': [0, 'Kuumailmapallo'],
               'medium_airport': [0, 'Keskikokoisia lento'],
               'large_airport': [0, 'Isoja lento']}

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'unna',
        password = 'salasana',
        autocommit = True,
        collation = 'utf8mb3_unicode_ci'
        )

maakoodi = input('Syötä maakoodi: ')
sqlTyyppi = (f'SELECT type FROM airport WHERE iso_country="{maakoodi}";')
sqlMaa = (f'SELECT name FROM country WHERE iso_country="{maakoodi}";')
kursori = yhteys.cursor()
kursori.execute(sqlTyyppi)
kentat = kursori.fetchall()

for k in kentat:
    if k[0] in kenttaLista:
        kenttaLista[k[0]][0]+=1

kursori.execute(sqlMaa)
maa = kursori.fetchall()

print(f'\n{maa[0][0]}ssa on:')
for kl in kenttaLista:
    if kenttaLista[kl][0]>0:
        print(kenttaLista[kl][1]+kenttiaTxt+str(kenttaLista[kl][0]))

#Anteeksi tiedän että "{maa[0][0]ssa" ei suurimmassa osassa tapauksista ole kieliopillisesti oikein
#Mutta se saa minut nauramaan
#Kentät ovat myös listattu satunnaisessa järjestyksessä sori