text = input("Введите послание: ")

no_space = ""  # Сохраняет текст без пробелов
for symbol in text:
    if symbol != " ":
        no_space += symbol

half_counter = len(no_space) // 2  # Длина половины текста без пробелов
fist_part = ""  # сохраняет первую половину текста без пробелов

for symbol in range(half_counter):
    fist_part += no_space[symbol]

reversed_text = "".join(reversed(no_space))  # Текст без пробелов в обратном порядке
second_part = ""  # Сохраняет вторую часть текста без пробелов в обратном порядке

for symbol in range(half_counter):
    second_part += reversed_text[symbol]

print(fist_part)
print(second_part)

if fist_part == second_part:
    print("Да, это палиндром!")

else:
    print("Нет, это не палиндром!")
