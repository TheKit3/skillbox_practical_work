x_pos = 8    # стартовая позиция по X
y_pos = 10    # стартовая позиция по Y

action = True

while action:
    move = input('').lower()

    if move == 'a':    # движение влево
        if x_pos > 1:
            x_pos -= 1

    elif move == 'd':    # движение вправо
        if x_pos < 20:
            x_pos += 1

    elif move == 'w':  # движение вверх
        if y_pos < 15:
            y_pos += 1

    elif move == 's':  # движение вниз
        if y_pos > 1:
            y_pos -= 1

    print('Марсоход находится на позиции:', x_pos, y_pos)
