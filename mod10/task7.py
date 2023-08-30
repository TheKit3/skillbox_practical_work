print('Задача 7. Пирамидка 2')

height = int(input("Введите высоту треугольника: "))
max_width = height * 2 - 1    # Вычисление максимальной ширины строки пирамиды


for row in range(1, height + 1):

    start_number = 1 + (row - 1) * 2  # Вычисление первого числа в текущем ряду
    row_width = row * 2 - 1 # Вычисление ширины текущего ряда
    padding = (max_width - row_width) // 2 # Вычисление количества пробелов для центрирования

    print(" " * padding, end="")   # Вывод пробелов перед числами для центрирования

   for col in range(row):  # Цикл для вывода чисел в текущем ряду

        print(start_number, end=" ")  # Вывод текущего числа и увеличение на 2 для следующего числа
        start_number += 2

    print()  # Переход на новую строку для следующего ряда

# мой код не работал как надо, гпт чат что-то с ним смог сделать, но все-равно печально центрирует пирамиду.
