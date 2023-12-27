def reverse():
    normal_number = input("Введите число: ")

    reversed_number = normal_number[::-1]
    print(int(reversed_number))
    if normal_number.startswith("0"):
        print("Ноль, который мы убрали, называется ведущим.")
    reverse()


reverse()


# добавить выход из функции при условии одного нуля при вводе