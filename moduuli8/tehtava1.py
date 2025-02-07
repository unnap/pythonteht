import mysql.connector

yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'unna',
        password = 'salasana',
        autocommit = True,
        collation='utf8mb3_unicode_ci'
        )

icao = input('Syötä ICAO: ')

sql = f'SELECT name, municipality FROM airport WHERE ident="{icao}"'
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(f'\nLentokenttä: {tulos[0][0]}\n'
        f'Kunta: {tulos[0][1]}')
