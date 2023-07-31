print("Задача 1. Тестовое задание")

# 0 2 4 6  8  10
# 1 3 5 7  9  11
# 2 4 6 8  10 12
# 3 5 7 9  11 13
# 4 6 8 10 12 14
# 5 7 9 11 13 15

for row in range(6):
    for col in range(0, 11, 2):
        print("\t", col + row, end="")
    print()
    