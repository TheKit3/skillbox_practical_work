print("Задача 3. Рамка")

width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

for row in range(width):
    for col in range(height):
        if col == 0 or col == height - 1:
            print("|", end="")
        elif row == 0 or row == width - 1:
            print("-", end="")
        else:
            print(" ", end="")
    print()
