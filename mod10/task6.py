print("Задача 6. Пирамидка")

height = int(input("Ввведите высоту треугольника: "))
symbol = "#"

for col in range(height):  # ну тут что-то слишком просто
    print(str(" " * height) + symbol)

    symbol += "##"
    height -= 1
