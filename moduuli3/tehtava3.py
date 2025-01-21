sex = input('Syötä biologinen sukupuolesi merkillä f tai m: ').casefold()
hemo = float(input('Syötä hemoglobiiniarvosi: '))

fLow = 117
mLow = 134
fHigh = 175
mHigh = 195

if sex=='f' or sex=='m':
    if (sex == 'f' and hemo<fLow or sex=='m' and hemo<mLow):
        print('Hempglobiinisi on alhainen')
    elif (sex=='f' and hemo>fHigh or sex=='m' and hemo>mHigh):
        print('Hemoglobiinisi on korkea')
    else:
        print('Hemoglobiinisi on normaali')
else:
    print('Virheellinen sukupuolimerkintä.')