leiviska = input('Leiviskät: ')
naula = input('Naulat: ')
luoti = input('Luodit: ')

le = float(leiviska) * 8512
na = float(naula) * 425.6
lu = float(luoti) * 13.3
summa = le+na+lu

print(f'Massa on {int(summa/1000)}kg {summa%1000:.2f}g')