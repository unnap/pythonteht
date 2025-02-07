import mysql.connector
from geopy.distance import geodesic


yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'unna',
        password = 'salasana',
        autocommit = True,
        collation = 'utf8mb3_unicode_ci'
        )

paikat = []

def hae_tiedot(icao):
    haePaikka = f'SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident="{icao}"'
    kursori = yhteys.cursor()
    kursori.execute(haePaikka)
    paikka = kursori.fetchall()
    return paikka

for i in range(2):
    icaoInput = input('Syötä ICAO: ')
    paikat.append(hae_tiedot(icaoInput))

ekaPaikka = (paikat[0][0][1], paikat[0][0][2])
tokaPaikka = (paikat[1][0][1], paikat[1][0][2])

print(f'\nKenttien {paikat[0][0][0]} ja {paikat[1][0][0]} välinen etäisyys on '
      f'{round(geodesic(ekaPaikka, tokaPaikka).km, 2)}km')