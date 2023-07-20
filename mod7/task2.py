year_salary = 0
months = 12

for salary in range(0, months):
    month_salary = int(input("Введите зарплату за месяц: "))
    year_salary += month_salary

average_salary = year_salary / months
print("Средняя зарплата за год составляет", average_salary)
