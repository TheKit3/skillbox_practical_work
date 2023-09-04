print("Задача 7. Пирамидка 2")

height = int(input("Введите высоту треугольника: "))

start_num = 1

for row in range(1, height + 1):
    print("\t" * (height - row), end="")

    for col in range(row):
        print(start_num, end=" ")
        start_num += 2
        print("\t" * 2, end="")

    print()
