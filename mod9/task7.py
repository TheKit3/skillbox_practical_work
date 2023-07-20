encrypted_word = input("Введите зашифрованное слово: ")

original_part1 = ""  # Первая часть слова в оригинале
reversed_part2 = ""  # Вторая часть слова в обратном порядке

for symbol in range(len(encrypted_word)):
    if symbol % 2 == 0:  # Все символы в нечетной последовательности 1 3 5 7 ...
        original_part1 += encrypted_word[symbol]

    else:  # Все символы в четной последовательности 2 4 6 8 ...
        reversed_part2 += encrypted_word[symbol]

original_part2 = "".join(reversed(reversed_part2))  #
original_word = original_part1 + original_part2

print(original_word)
