deep = int(input('Введите число: '))
K = deep

for row in range(deep, 0, -1):

    # Печатаем убывающую последовательность чисел
    for Col in range(deep, deep - row, -1):
        print(Col, end="")

    # Заполняем промежуток точками
    for dots in range(2 * row - 2):
        print(".", end="")

    # Печатаем возрастающую последовательность чисел
    for coL in range(deep - row + 1, deep + 1):
        print(coL, end="")

    print()
