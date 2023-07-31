print('Задача 2. Лестница')

N = int(input("Введите число: "))

for row in range(N + 1):
    for col in range(row):
        print(row, end=" ")
    print()
