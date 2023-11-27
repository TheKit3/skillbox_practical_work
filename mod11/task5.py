!
print('Задача 5. Вот это объёмы!')

import math

planet_radius = float(input("Введите радиус случайной планеты: "))

# объем Земли

earth_volume = float(1.08321 * 10 ** 12)

# посчитаем объем планеты по формуле V = 4/3 * Pi * R^3

planet_volume = float(4 / 3 * math.pi * planet_radius ** 3)

# сравним объем планеты с объемом планеты Земля

if planet_volume > earth_volume:

    print("Объем планеты Земля меньше в", (1, round(earth_volume / planet_volume, 3)), round(planet_volume / earth_volume, 3), "раз")

elif planet_volume < earth_volume:

    print("Объем планеты Земля больше в ", round(earth_volume / planet_volume, 3), "раз")

else:

    print("Планеты равны в объеме.")
