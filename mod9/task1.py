new_pirats = 0

for speak in range(10):
    hello = input('Крик пирата: ').lower()    # Немножко прокачаемся :)
    if hello == 'карамба':
        new_pirats += 1

print('Новых пиратов:', new_pirats)
