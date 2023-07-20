n = int(input("Введите N: "))
elem_sum = 0  # сумма элементов последовательности

for value in range(n):
    elem_sum += (-1) ** value * 0.5**value

print("Ответ:", elem_sum)
