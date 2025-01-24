tunnus = 'python'
salasana = 'rules'
yritykset = 0

inputTunnus = input('Käyttäjätunnus: ')
inputSalasana = input('Salasana: ')

while tunnus!=inputTunnus and salasana!=inputSalasana and yritykset<4:
    print('\nSalasana ja käyttäjänimi ei täsmää\n')
    yritykset+=1

    inputTunnus = input('Käyttäjätunnus: ')
    inputSalasana = input('Salasana: ')

if not(tunnus!=inputTunnus and salasana!=inputSalasana):
    print('\nTervetuloa!')
else:
    print('\nPääsy evätty')