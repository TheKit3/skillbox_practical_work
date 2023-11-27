!
import math

error_message = "Неверный формат данных"

while True:
    try:
        start_position_x = float(input("Введите положение коня на доске: "))
        if start_position_x >= 0.0 and start_position_x <= 8.0:
            break
        else:
            print()
            print("Вы вышли за границу доски. Введите другое значение")
    except ValueError:
        print()
        print(error_message)

while True:
    try:
        start_position_y = float(input("Введите положение коня на доске: "))
        if start_position_y >= 0.0 and start_position_y <= 8.0:
            break
        else:
            print()
            print("Вы вышли за границу доски. Введите другое значение")
    except ValueError:
        print()
        print(error_message)

while True:
    try:
        finish_position_x = float(input("Введите позицию на которую вы хотите переместить коня"))
        if finish_position_x >= 0.0 and finish_position_x <= 8.0:
            break
        else:
            print()
            print("Вы вышли за границу доски. Введите другое значение")
    except ValueError:
        print()
        print(error_message)
while True:
    try:
        finish_position_y = float(input("Введите позицию на которую вы хотите переместить коня"))
        if finish_position_y >= 0.0 and finish_position_y <= 8.0:
            break
        else:
            print()
            print("Вы вышли за границу доски. Введите другое значение")
    except ValueError:
        print()
        print(error_message)

print(start_position_x)
print(start_position_y)
print(finish_position_x)
print(finish_position_y)
