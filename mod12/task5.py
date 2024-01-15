def count_letters():
    enterText = input("Введите текст: ")

    digitSearcher = int(input("Какую цифру ищем? "))
    counter1 = 0
    for i in enterText:
        if i == str(digitSearcher):
            counter1 += 1

    letterSearcher = input("Какую букву ищем? ")
    counter2 = 0
    for i in enterText:
        if i == letterSearcher:
            counter2 += 1

    print("Количество цифр", str(digitSearcher) + ":", counter1)
    print("Количество букв", letterSearcher + ":", counter2)


count_letters()
