import random

autot = []
seperator1 = '----***----'
seperator2 = '---'

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

def kilpa():
    loppu = False

    while not loppu:
        for a in autot:
            a.kiihdyta(round(random.uniform(-10, 15), 2))
            a.kulje(1)
            if a.matka >= 10000:
                loppu = True

    autot.sort(key=lambda a: a.matka, reverse=True)

    for a in autot:
        if autot.index(a)==0:
            print('Ensimmäinen sija')
            print(seperator1)
        elif autot.index(a)==1:
            print('Toinen sija')
            print(seperator1)
        elif autot.index(a)==2:
            print('Kolmas sija')
            print(seperator1)
        else:
            print(autot.index(a)+1)
            print(seperator2)

        a.naytaTiedot()
        print('')

for i in range(10):
    autot.append(Auto(f'ABC-{i+1}', round(random.uniform(100, 200), 0)))

kilpa()