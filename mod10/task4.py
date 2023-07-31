qDigits = int(input('Введите количество цифр: '))
prime_numbers = 0
dividers = 0

for num in range(qDigits):
    number = int(input("Введите число: "))
    for N in range(1, number):
        if number % N == 0:
            dividers += 1
            if dividers > 2:
                dividers = 0
            else:
                prime_numbers += 1
                dividers = 0

print(prime_numbers)