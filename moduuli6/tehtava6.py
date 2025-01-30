import math

#Vastaus vähän poikkeaa tehtävänannosta koska halusin harjoitella

pitsojenLukum = int(input('Anna vertailtavien pitsojen lukumäärä: '))
pitsat = []
pitsaNro = 1

def pitsa(d,e):
    pitsaPintaala = (math.pi/4)*float(d)**2/1000
    pitsaJaHinta = [pitsaNro, float(e)/pitsaPintaala]
    return pitsaJaHinta

def hintavertailu():
    halvempi = pitsat[0]
    kalliimpi = pitsat[0]

    for i in range(len(pitsat)):
        if pitsat[i][1]<halvempi[1]:
            halvempi = pitsat[i]
        elif pitsat[i][1]>kalliimpi[1]:
            kalliimpi = pitsat[i]
    hinnat = [halvempi, kalliimpi]
    return hinnat


for i in range(pitsojenLukum):
    halkaisija = input(f'Pitsa {pitsaNro} halkaisija senttimetreinä: ')
    euro = input(f'Pitsa {pitsaNro} hinta: ')
    pitsat.append(pitsa(halkaisija, euro))
    pitsaNro+=1

pitsatFinal = hintavertailu()

print(f'\nPitsoista parhaan vastineen antaa pitsa {pitsatFinal[0][0]} arvolla {pitsatFinal[0][1]:.2f} €/m2'
      f'\nPitsa {pitsatFinal[1][0]} on kallein arvolla {pitsatFinal[1][1]:.2f} €/m2')

#liian monta pitsa-muuttujaa...