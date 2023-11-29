print("Задача 1. Конвертация")

import math

priceEuro = float(input("Введите стоимость товара в евро: "))

priceUSD = math.ceil(priceEuro * 1.25 * 100) / 100

priceRUB = math.ceil(priceUSD * 60.87 * 100) / 100

print("Цена покупки составит:", priceRUB)
