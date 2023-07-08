boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

total = boys + girls    # Общее количество
line = str()     # рассадка

if boys == girls:
    for set in range(total // 2):
        line += 'B'
        line += 'G'

elif boys > girls:
    large_group = boys
    smaller_group = girls
    large_count = 'B'
    smaller_count = 'G'

elif girls > boys:
    large_group = girls
    smaller_group = boys
    large_count = 'G'
    smaller_count = 'B'

else:

print(line)
