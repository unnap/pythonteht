class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus, matka):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        self.huippunopeus_show = f'{self.huippunopeus} km/h'

    def kiihdyta(self, muutos):
        if self.nopeus+muutos<0.0:
            self.nopeus = 0.0
        elif self.nopeus+muutos>self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus+=muutos
        return

    def kulje(self, tunnit):
        self.matka+= self.nopeus*tunnit
        return

    def naytaTiedot(self):
        print(f'{self.rekisteri}\n'
              f'{self.huippunopeus:.0f} km/h\n'
              f'{self.nopeus} km/h\n'
              f'{self.matka} km')

auto = Auto('ABC-123', 142.0, 60.0, 2000.0)

auto.kulje(1.5)
auto.naytaTiedot()