text = input('Введите текст: ')
symbol_counter = 0
big_word = 0

for symbol in text:

    if symbol != ' ':
        symbol_counter += 1    # Пока у нас нет пробела - считаем символы

    else:
        if big_word < symbol_counter:    # тут сравниваем значения, и наибольшее записываем в big_word
            big_word = symbol_counter
        symbol_counter = 0    # И обнуляем нашу переменную под счетчтик

print(big_word)
