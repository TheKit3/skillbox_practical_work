print('Задача 7. Пирамидка 2')

height = int(input("Ввведите высоту треугольника: "))

start_number = 1

for row in range(height):
    for col in range(row):
        print(start_number, end="")
    print()
