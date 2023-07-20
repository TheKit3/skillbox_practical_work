text = input("Введите текст со звездочкой: ")
asterisk = "\nСимвол «*» стоит на позиции: "
pos_counter = 0  # Считает позицию
presence_aster = False  # Переключатель для вывода ответа

for symbol in text:
    pos_counter += 1
    if symbol == "*":
        presence_aster = True
        break

if presence_aster:
    print(asterisk, pos_counter)

else:
    print("«*» - нет.")  # немного улучшил, чтобы без звездочек тоже работало
