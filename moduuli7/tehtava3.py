lentoasemat = {'EFHK':'Helsinki-Vantaan lentoasema',
               'EFTP':'Tampere-Pirkkalan lentoasema',
               'EFRO':'Rovaniemen lentoasema'}

kysely = int(input('1 = Lisää lentokenttä listaan'
                   '\n2 = Tarkastele lentokenttiä'
                   '\n3 = Lopeta'
                   '\nSyötä numero: '))
lopetus = False
i=0

while not lopetus:
    if kysely==1:
        ICAO = input('Syötä ICAO-koodi: ').upper()
        lentokentta = input('Syötä lentokentän nimi: ')
        lentoasemat[ICAO] = lentokentta

        print(f'{lentokentta} lisätty listaan')
        kysely = int(input('\nSyötä numero: '))

    elif kysely==2:
        asematListassa = '\nICAO koodit listassa:'
        for l in lentoasemat:
            i+=1
            if i!=len(lentoasemat):
                asematListassa+=' '+l+','
            else:
                asematListassa += ' ' + l
        print(asematListassa)

        ICAO = input('\nSyötä ICAO-koodi jota haluat tarkastella: ').upper()
        if ICAO in lentoasemat:
            print(lentoasemat[ICAO])
        else:
            print('Virheellinen koodi')
        kysely = int(input('\nSyötä numero: '))

    elif kysely==3:
        print('Kiitti mo')
        lopetus = True
    else:

        print('\nVirheellinen numero')
        kysely = int(input('1 = Lisää lentokenttä listaan'
                           '\n2 = Tarkastele lentokenttiä'
                           '\n3 = Lopeta'
                           '\nSyötä numero: '))