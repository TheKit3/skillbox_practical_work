educational_grant = int(input('Введите степендию: '))
expenses = int(input('Введите стоимость жилья: '))
parental_sup = 0    # Сколько попросим у родителей

for month in range(1, 11):

    lack = expenses - educational_grant    # сколько денег не хватает в месяц

    print('{}.'.format(month), 'месяц траты ', '%.2f' % expenses, ' не хватает ', '%.2f' % lack)
    expenses += expenses / 100 * 3    # увеличиваем размер ежемесечного расхода
    parental_sup += lack

print()
print('Нужно попросить у родителей', '%.2f' % parental_sup, 'рублей.')
