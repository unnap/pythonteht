import requests

haku = input('Syötä paikkakunta: ')
avain = '825506bf16a1f2ac2f76af93677e0eb3'
raja = 5
print('')

try:
    paikkaPyynto = f'http://api.openweathermap.org/geo/1.0/direct?q={haku}&limit={raja}&appid={avain}'
    paikkaVastaus = requests.get(paikkaPyynto)

    if paikkaVastaus.status_code==200:
        paikka = paikkaVastaus.json()

        if len(paikka)==0:
            print('Ei hakutuloksia')
        else:
            lat = paikka[0]['lat']
            lon = paikka[0]['lon']

            try:
                saaPyynto = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={avain}'
                saaVastaus = requests.get(saaPyynto)

                if saaVastaus.status_code==200:
                    saa = saaVastaus.json()
                    try:
                        print(f'{paikka[0]["local_names"]["fi"]}n sää:')
                        lampotila = 'Lämpötila'
                        tuntuuKuin = 'Tuntuu kuin'
                    except:
                        print(f'Weather in {paikka[0]["name"]}')
                        lampotila = 'Temperature'
                        tuntuuKuin = 'Feels like'
                    print('---------')
                    print(saa['weather'][0]['main'])
                    print(f'{lampotila}: {round(saa["main"]["temp"]-273.15)}\n'
                          f'{tuntuuKuin}: {round(saa["main"]["feels_like"]-273.15)}')

            except requests.exceptions.RequestException as e:
                print('Haku ei onnistunut')

except requests.exceptions.RequestException as e:
    print('Haku ei onnistunut')