reverse_timer = int(input('Введите время приготовления: '))
hot_food = True    # Для еды прошедшей через весь цикл

for sec in range(reverse_timer, 0, -1):

    print(sec)
    readiness = int(input('Еда готова? '))

    if readiness == 0:    # Если не готова - продолжаем
        continue

    elif readiness == 1:    # Если готова - выходим из цикла, выходим из цикла и сообщаем о готовности
        hot_food = False
        print('Ваша еда готова, можете забрать')
        break

if hot_food:    # Условие hot_food не нарушено выводим финальную фразу
    print(0)
    print('Ваша еда готова, осторожно горячo!')
