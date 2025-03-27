class Auto:
    lukum=0

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
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

class Sahkoauto(Auto):

    def __init__(self, rekisteri, huippunopeus, akku):
        super().__init__(rekisteri, huippunopeus)
        self.akku = akku

    def naytaTiedot(self):
        super().naytaTiedot()
        print(f'{self.akku} kWh')

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteri, huippunopeus, tankki):
        super().__init__(rekisteri,huippunopeus)
        self.tankki = tankki
    def naytaTiedot(self):
        super().naytaTiedot()
        print(f'{self.tankki} l')

s = Sahkoauto('ABC-15',180.0,52.5)
p = Polttomoottoriauto('ACD-123',165.0,32.3)

s.kiihdyta(80.0)
p.kiihdyta(120.0)
s.kulje(3)
p.kulje(3)

print('')
s.naytaTiedot()
print('\n======================\n')
p.naytaTiedot()