boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

total = boys + girls
line = str()

if boys == girls:
    for set in range(boys):
        line += 'BG'

elif boys > girls:
    if boys - girls <= 2:
        for set in range(total // girls):
            line += 'BGB'
        line += 'BG'
    else:
        print('Ответ: Нет решения.')

   # elif boys < girls:

print(line)
