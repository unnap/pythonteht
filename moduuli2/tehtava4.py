print('Syötä numerot kokonaislukuina')
ekastr = input('Syötä numero: ')
tokastr = input('Syötä toinen numero: ')
kolmasstr = input('Syötä kolmas numero: ')

eka = int(ekastr)
toka = int(tokastr)
kolmas = int(kolmasstr)

print(f'\nSumma: {eka+toka+kolmas}'
      f'\nTulo: {eka*toka*kolmas}'
      f'\nKeskiarvo: {(eka+toka+kolmas)/3:.0f}')