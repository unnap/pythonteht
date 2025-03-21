class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus_show = f'{self.huippunopeus} km/h'

    def kiihdyta(self, muutos):
        if self.nopeus+muutos<0:
            self.nopeus = 0
        elif self.nopeus+muutos>self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus+=muutos
        return

    def naytaTiedot(self):
        print(f'{self.rekisteri}\n'
              f'{self.huippunopeus} km/h\n'
              f'{self.nopeus} km/h\n'
              f'{self.matka} km')

auto = Auto('ABC-123', 142)

auto.kiihdyta(30)
#print(auto.nopeus)
auto.kiihdyta(70)
#print(auto.nopeus)
auto.kiihdyta(50)
#print(auto.nopeus)
auto.kiihdyta(-200)
print(auto.nopeus)

#auto.naytaTiedot()