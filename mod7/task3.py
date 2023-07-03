print('Задача 3. Факториал')

n = int(input('Посчитаю факториал числа: '))
x = str(n)
result = 1

if n < 0:
    print('Факториал можно вычислить только для целого положительного числа')
else:
    for factorial in range(0, n):
        result *= n
        n -= 1
    print(x + '! = ' + str(result))
