class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        self.kerros+=1
        print(self.kerros)
    def kerros_alas(self):
        self.kerros-=1
        print(self.kerros)

    def siirry_kerrokseen(self, k):
        if k>self.ylin or k<self.alin:
            print('kyseistä kerrosta ei ole olemassa')
        else:
            while k != self.kerros:
                if k>self.kerros:
                    self.kerros_ylos()
                elif k<self.kerros:
                    self.kerros_alas()
            print('Olet perillä')

h = Hissi(1,7)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin)