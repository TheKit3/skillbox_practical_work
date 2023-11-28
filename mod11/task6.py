import math

def value_restriction(z):
    while True:
        try:
            z = float(input())
            if 0.0 <= z <= 0.8:
                return(z)
            else:
                print("Вы вышли за пределелы доски, попробуйте другое значение:")
        except ValueError:
            print("Вы ввели недопустимое значение, попробуйте снова:")

x_start = float()
y_start = float()
x_end = float()
y_end = float()

print("Введите местоположение коня:")
x_start_position = value_restriction(x_start)
y_start_position = value_restriction(y_start)

print("Введите местоположение точки на доске:")
x_end_position = value_restriction(x_end)
y_end_position = value_restriction(y_end)

# вычислим разницу
x_movement_difference = abs(int(x_start_position * 10) - int(x_end_position * 10))
y_movement_difference = abs(int(y_start_position * 10) - int(y_end_position * 10))

if ((x_movement_difference == 2 and y_movement_difference == 1)
        or (x_movement_difference == 1 and y_movement_difference == 2)):
    print("Ход возможен.")
else:
    print("Ход невозможен!")