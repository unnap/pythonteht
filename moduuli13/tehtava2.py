import mysql.connector
from flask import Flask
import json

app = Flask(__name__)
@app.route('/kentta/<icao>')
def kentta(icao):
        icao = icao.upper()
        print(icao)
        try:
                yhteys = mysql.connector.connect(
                        host = '127.0.0.1',
                        port = 3306,
                        database = 'flight_game',
                        user = 'root',
                        password = '1234',
                        autocommit = True,
                        collation='utf8mb3_unicode_ci'
                        )

                sql = f'SELECT name, municipality FROM airport WHERE ident="{icao}"'
                kursori = yhteys.cursor()
                kursori.execute(sql)
                tulos = kursori.fetchall()
                txt = {
                        'ICAO': icao,
                        'Name': tulos[0][0],
                        'Municipality': tulos[0][1]
                }

        except ValueError:
                txt = {
                        'teksti': 'jotain meni pieleen'
                }
        jsontxt = json.dumps(txt)
        return jsontxt

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)