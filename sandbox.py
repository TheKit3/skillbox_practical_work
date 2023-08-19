print('Задача 7. Пирамидка 2')

height = int(input("Ввведите высоту треугольника: "))

start_number = 1

for row in range(1, height + 1):

    spaces = " " * (height - row)
    row = spaces

    for col in range(row):

        print(start_number, end=" ")

        start_number += 2
        row -= 1

    print()
