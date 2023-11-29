print("Задача 4. Первая цифра")

x = float(input("Введите число: "))

y = int(round(x - int(x), 1) * 10)  # первая цифра после запятой

print(y)
