# Простое число делиться только на 1 и на себя (имеет 2 делителя).

qDigits = int(input('Введите количество цифр: '))
prime_numbers = 0    # количесто простых чисел
dividers = 0    # количество целочисленных делителей

for num in range(qDigits):
    number = int(input("Введите число: "))

    for N in range(1, number + 1):
        print("\nделим на", N)
        print("остаток от деления", number % N)
        if number % N == 0:
            dividers += 1
            print("количество делителей", dividers)

        if dividers == 2:
            prime_numbers += 1

        dividers = 0
    print(prime_numbers)

print("Простых чисел:", prime_numbers)
