import math

def value_restriction(z):
    while True:
        try:
            z = float(input("Введите значение: "))
            if 0.0 <= z <= 8.0:
                return(z)
            else:
                print("Вы вышли за пределелы доски, попробуйте другое значение.")
        except ValueError:
            print("Вы ввели недопустимое значение: ")

x_start = float()
y_start = float()
x_end = float()
y_end = float()

x_start_position = value_restriction(x_start)
y_start_position = value_restriction(y_start)
x_end_position = value_restriction(x_end)
y_end_position = value_restriction(y_end)

# вычислим разницу
x_movement_difference = abs(int(x_start_position * 10) - int(x_end_position * 10))
y_movement_difference = abs(int(y_start_position * 10) - int(y_end_position * 10))

if x_movement_difference == 2 and y_movement_difference == 2:
    print("Ход возможен.")
else:
    print("Ход невозможен!")