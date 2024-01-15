print("Задача 7. Пирамидка 2")

height = int(input("Введите высоту треугольника: "))

max_width = height * 2 - 1

for row in range(1, height + 1):
    start_number = 1 + (row - 1) * 2
    row_width = row * 2 - 1
    padding = (max_width - row_width) // 2

    print(" " * padding, end="")

    for col in range(row):
        print(start_number, end=" ")
        start_number += 2

    print()
