number = int(input("Введите число: "))
num_counter = 0

while number != 0:
    num_counter += number % 10
    number //= 10

print("Сумма чисел:", num_counter)
