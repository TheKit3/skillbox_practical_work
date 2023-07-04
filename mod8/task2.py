debtors = int(input('ВВедите количество должников: '))
debt_amount = 0

for debtor in range(0, debtors, 5):
    print('Должник с номером: ', debtor)
    debt = int(input('Сколько должны? '))
    debt_amount += debt

print()
print('Общая сумма задолженности составляет:', debt_amount, 'рублей')
