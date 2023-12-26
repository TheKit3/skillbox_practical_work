def calculator():

    NumberInQuestion = int(input("Введите число: "))

    print("Действие с числом: ")
    print("1 - Вывести сумму его чисел.")
    print("2 - Максимальную цифру.")
    print("3 - Минимальную цифру.")

    choice = int(input())
    if choice == 1:
        SumOfDigits(NumberInQuestion)

    elif choice == 2:
        maximum_figure(NumberInQuestion)

    elif choice == 3:
        minimum_figure(NumberInQuestion)

    else:
        print("Ошибка вввода. Выберите доступный вариант (1, 2, 3)")

    print()
    calculator()

def SumOfDigits(x):
    sum_result = 0
    while x > 0:
        sum_result += x % 10
        x //= 10
    print(sum_result)

def maximum_figure(x):
    number_str = str(x)
    max_digit = 0
    for digit in number_str:
        current_digit = int(digit)
        if current_digit > max_digit:
            max_digit = current_digit
    print("Максимальная цифра числа равна", max_digit)
def minimum_figure(x):
    number_str = str(x)
    min_digit = 9
    for digit in number_str:
        current_digit = int(digit)
        if current_digit < min_digit:
            min_digit = current_digit

    print("Минимальная цифра числа равна", min_digit)

calculator()
