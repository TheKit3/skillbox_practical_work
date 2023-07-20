a = int(input("a = "))  # начало отрезка
b = int(input("b = "))  # конец отрезка
c = int(input("c = "))  # кратность


for dot in range(a, b):  # как-то так
    if dot % c == 0:
        print(dot)
