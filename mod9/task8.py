text = input("Введите послание: ")

no_space = ''  # Сохраняет текст без пробелов
for symbol in text:
    if symbol != ' ':
        no_space += symbol

print(no_space)

half_counter = len(no_space) // 2  # Длина половины текста без пробелов

fist_part = ''    # сохраняет первую половину текста без пробелов
for symbol in range(half_counter):
    fist_part += symbol

second_part = ''.join(reversed(no_space))

print(second_part)

#if fist_part == second_part:
   # print('Да, это палиндром!')

#else:
   # print('Нет, это не палиндром!')
