print("Задача 2. Грубая математика")

import math

amountNum = int(input("Введите колличество цифр: "))

for num in range(amountNum):
    number = float(input("Ввведите число: "))
    if number > 0:
        print("x =", math.ceil(number), "lox(x) =", math.log(math.ceil(number)))

    if number < 0:
        print("x =", math.floor(number), "exp(x) =", math.e ** math.floor(number))
