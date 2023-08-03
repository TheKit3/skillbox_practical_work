print("Задача 5. Наибольшая сумма цифр")

amount = int(input("ВВедите количетсво чисел: "))

num_counter = 0  # Счетчик суммы цифр
big_num_counter = 0  # Наибольшая сумма цифр
remember_num = 0  # Запомним
big_num = 0  # Наибольшее число 2

for numbers in range(amount):
    number = int(input("Введите число: "))
    remember_num = number    # сохраняем в переменную для того чтобы не потерять наше число

    while number != 0:    # считаем и отбрасываем знаки
        num_counter += number % 10
        number //= 10

    if num_counter > big_num_counter:  # Если счетчик больше, чем наибольшая сумма
        big_num_counter = num_counter  # счетчик -> наибольшей суммой
        big_num = remember_num  # изначальное число -> наибольшее

    num_counter = 0  # сбрасываем счетчик

print("Наибольшее число:", big_num, "\nСумма его чисел:", big_num_counter)
