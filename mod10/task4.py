print("Задача 4. Простые числа")

# Простое число делиться только на 1 и на себя (имеет 2 делителя).

qDigits = int(input("Введите количество цифр: "))
prime_numbers = 0  # количесто простых чисел
dividers = 0  # количество целочисленных делителей

for num in range(qDigits):  # цикл для перебора чисел
    number = int(input("Введите число: "))

    for N in range(1, number + 1):  # берем число из цикла
        if number % N == 0:  # если оно делится без остатка
            dividers += 1  # увеличиваем количество делителей

    if dividers == 2:  # Если количество делителей у числа рано двум
        prime_numbers += 1  # Увеличиваем количество простых чисел в последовательности

    dividers = 0  # сбрасываем счетчик перед новым проходм

print("Количество простых чисел в последовательности:", prime_numbers)
