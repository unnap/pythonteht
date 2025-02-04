print('Tyhjän rivin tulostaminen pysäyttää ohjelman')
nimet = set()
nimi = input('Anna nimi: ').capitalize()

while nimi!='':
    if nimi in nimet:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
    nimet.add(nimi)
    nimi = input('\nAnna nimi: ').capitalize()

print('\nAnnetut nimet:')
for n in nimet:
    print(n)