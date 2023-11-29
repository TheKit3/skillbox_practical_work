print("Задача 3. Аналог Steam")

import time

file_size = int(input("Введите размер файла в Мб: "))
net_speed = int(input("Введите скорость вашего соединения в Мб/с: "))

download_time = int(file_size / net_speed)  # Время скачивания в секундах
perсent = 0

if file_size < net_speed:
    print()
    print("Скачано", file_size, "из", file_size, "Мб (100%)")

else:
    for i in range(1, download_time + 1):
        time.sleep(1)
        perсent = int(net_speed * i / file_size * 100)
        print(
            "Прошло",
            i,
            "секунд. Скачано",
            net_speed * i,
            "из",
            file_size,
            "Мб",
            "(" + str(perсent) + "%)",
        )

    if file_size % net_speed != 0:
        time.sleep(1)
        print(
            "Прошло", i + 1, "секунд. Скачано", file_size, "из", file_size, "Мб (100%)"
        )
