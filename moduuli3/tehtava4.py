vuosi = int(input('Anna vuosi: '))
karkausvuosi = f'{vuosi} on karkausvuosi'

if vuosi%4==0 and vuosi%100!=0:
    print('karkausvuosi')
elif vuosi%400==0:
    print('karkausvuosi')
else:
    print(f'{vuosi} ei ole karkausvuosi')