N = int(input("Введите число: "))

for row in range(N):
    for col in range(row, N):
        print(col, end="")
    print()
