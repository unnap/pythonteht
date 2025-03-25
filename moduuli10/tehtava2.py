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

class Talo:
    hissit= []

    def __init__(self, alin, ylin, hissiLkm):
        self.alin = alin
        self.ylin = ylin
        for i in range(hissiLkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissiNro, kohde):
        if hissiNro>len(self.hissit) or hissiNro<1:
            print('Kyseistä hissiä ei ole olemassa')
        else:
            self.hissit[hissiNro-1].siirry_kerrokseen(kohde)

t = Talo(1,7,3)

t.aja_hissia(1,3)
t.aja_hissia(2,4)
t.aja_hissia(3,t.ylin)
t.aja_hissia(1,t.alin)