luku = input('Anna luku: ')
luvut = []

while True:
    luvut.append(int(luku))
    luku = input('Anna luku: ')
    if luku == '':
        break

luvut.sort(reverse=True)

if len(luvut)==1:
    teksti = '\nSuurin luku on'
else:
    teksti = '\nSuurimmat luvut ovat'

if len(luvut)<5:
    for luku in range(len(luvut)):
        teksti += f' {luvut[luku]}'
else:
    for luku in range(5):
        teksti += f' {luvut[luku]}'

print(teksti)