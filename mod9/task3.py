rows = int(input("Введите количество рядов: "))
sets_row = int(input("Введите количество сидений в ряде: "))
distance = int(input("Введите расстояние между рядами: "))

print("\nСцена")

for row in range(rows):
    print(sets_row * "=", distance * "*", sets_row * "=")
