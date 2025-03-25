import random

autot = []

class Auto:
    lukum=0

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus_show = f'{self.huippunopeus} km/h'
        Auto.lukum+=1

    def kiihdyta(self, muutos):
        if self.nopeus+muutos<0:
            self.nopeus = 0
        elif self.nopeus+muutos>self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = round(self.nopeus + muutos, 2)
        return

    def kulje(self, tunnit):
        self.matka = round(self.matka + self.nopeus*tunnit, 2)
        return

    def naytaTiedot(self):
        print(f'{self.rekisteri}\n'
              f'{self.huippunopeus:.0f} km/h\n'
              f'{self.nopeus} km/h\n'
              f'{self.matka} km')


class Kilpailu:
    separator1 = '----***----'
    separator2 = '---'
    separator3 = '=================='
    separator4 = '~~~~~~~~~~~~~~~~~~'

    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat
        self.kulunutAika = 0

    def tulosta_tilanne(self):
        self.osallistujat.sort(key=lambda o: o.matka, reverse=True)

        print('')
        print(self.separator3)
        print(f'Aikaa kulunut {self.kulunutAika}h')
        print(self.separator3)
        print('')

        for o in self.osallistujat:
            if self.osallistujat.index(o) == 0:
                print('Ensimmäinen sija')
                print(self.separator1)
            elif self.osallistujat.index(o) == 1:
                print('Toinen sija')
                print(self.separator1)
            elif self.osallistujat.index(o) == 2:
                print('Kolmas sija')
                print(self.separator1)
            else:
                print(self.osallistujat.index(o) + 1)
                print(self.separator2)

            o.naytaTiedot()
            print('')

    def tunti_kuluu(self):
        for o in self.osallistujat:
            o.kiihdyta(round(random.uniform(-10, 15), 2))
            o.kulje(1)

        self.kulunutAika+=1
        if self.kulunutAika%10==0:
            self.tulosta_tilanne()

    def kilpailu_ohi(self):
        for o in self.osallistujat:
            if o.matka>=self.pituus:
                print('')
                print(self.separator3)
                #print(self.separator4)
                #Minulla oli hankaluuksia päättää kumpi separator on kivempi tässä
                #Joten jätin tuon toisen kummittelemaan tähän kommenttina
                #nyt vasta muuten googlesin kirjoitetaanko se seperator vai separator
                #vanhassa tehtävässä se on vielä seperator RIP saanko miinuksia huonosta enkusta
                print('')
                print('VIIMEISET TULOKSET')
                self.tulosta_tilanne()
                print('Onnittelut kaikille osallistujille!')
                return True
        return False

    def aloita_kilpailu(self):
        print(f'\n{self.nimi} alkaa nyt!')
        while not self.kilpailu_ohi():
            self.tunti_kuluu()


for i in range(10):
    autot.append(Auto(f'ABC-{i+1}', round(random.uniform(100, 200), 0)))

romuralli = Kilpailu('Suuri Romuralli', 8000.00, autot)
romuralli.aloita_kilpailu()