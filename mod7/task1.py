even_positive = 0

for users in range(0, 10):
    user_number = int(input("Введите номер человека: "))
    if user_number > 0 and user_number % 2 == 0:
        even_positive += 1
print(even_positive)
