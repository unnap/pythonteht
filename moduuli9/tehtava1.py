class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def naytaTiedot(self):
        print(f'{self.rekisteri}\n'
              f'{self.huippunopeus} km/h\n'
              f'{self.nopeus} km/h\n'
              f'{self.matka} km')

auto = Auto('ABC-123', '142')

auto.naytaTiedot()