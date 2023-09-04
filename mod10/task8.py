deep = int(input("Введите число: "))
K = deep

for row in range(1, deep + 1):
    # Печатаем убывающую последовательность чисел
    for Col in range(deep, deep - row, -1):
        print(Col, end="")

    # Заполняем промежуток точками
    for dots in range(K * 2 - 2):
        print(".", end="")

    # Печатаем возрастающую последовательность чисел
    for coL in range(deep - row + 1, deep + 1):
        print(coL, end="")

    K -= 1  # Методом тыка пришел к этому :)
    print()
