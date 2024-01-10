def reverse():
    normal_number = input("Введите число: ")

    if normal_number == "0":
        print("Программа завершена!")

    elif int(normal_number) % 10 == 0:

        reversed_number = normal_number[:-1][::-1]    # убираем последний элемент и переворачиваем последовательность
        print(int(reversed_number))
        print("Ноль, который мы убрали, называется ведущим.")
        reverse()

    else:
        reversed_number = normal_number[::-1]    # переворачиваем последовательность
        print(int(reversed_number))
        reverse()

reverse()
