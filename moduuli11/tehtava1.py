class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivum):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivum = sivum

    def print_info(self):
        print(f'{self.nimi}\n'
              f'Kirjoittaja: {self.kirjoittaja}\n'
              f'Sivumäärä: {self.sivum}')

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def print_info(self):
        print(f'{self.nimi}\n'
              f'Päätoimittaja: {self.paatoimittaja}')


akkari = Lehti('Aku Ankka', 'Aki Hyyppä')
hytti6 = Kirja('Hytti n:o 6','Rosa Liksom',200)

print('')
akkari.print_info()
print('\n======================\n')
hytti6.print_info()