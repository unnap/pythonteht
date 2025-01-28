print('Anna viiden kaupungin nimet')
kaupunki = input('Kaupunki 1: ')
kaupungit = [kaupunki]

for k in range(4):
    kaupunki = input(f'Kaupunki {k+2}: ')
    kaupungit.append(kaupunki)

print('\nKaupungit joissa haluaisin käydä:')

for k in kaupungit:
    print(k)