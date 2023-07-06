educational_grant = int(input('Введите степендию: '))
expenses = int(input('Введите стоимость жилья: '))

for month in range(1, 11):

    lack = expenses - educational_grant

    print(month, 'месяц траты ', expenses, ' не хватает ', lack)

    expenses += expenses / 100 * 3



