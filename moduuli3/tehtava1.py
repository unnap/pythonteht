kuha = float(input('Kuhan pituus sentteinä: '))

if kuha<37:
    print(f'Kuhasi on {37-kuha:.2f}cm liian pieni, päästä se takas järveen')
else:
    print('Kuhasi on ' + str(kuha) + 'cm')