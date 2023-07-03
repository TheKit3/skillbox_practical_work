wake_up = int(input('Во сколько проснулся: '))
water = 0
calories_sum = 0

for hour in range(wake_up, 23, 3):
    water += 1
    water('Пошли есть в', hour, 'часов')
    calories = int(input('Сколько съел?'))
    calories_sum += calories
print('Выпито литров воды:' water )