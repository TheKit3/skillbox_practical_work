def rock_paper_scissors():
    player_choise1 = str(input("Первый игрок выбирает: камень, ножницы или бумага: "))
    player_choise2 = str(input("Второй игрок выбирает: камень, ножницы или бумага: "))

    if player_choise1.lower() == "камень" and player_choise2.lower() == "бумага":
        print("Второй игрок победил!")
    elif player_choise1.lower() == "бумага" and player_choise2.lower() == "камень":
        print("Первый игрок победил!")
    elif player_choise1.lower() == "камень" and player_choise2.lower() == "ножницы":
        print("Первый игрок победил!")
    elif player_choise1.lower() == "ножницы" and player_choise2.lower() == "камень":
        print("Второй игрок победил!")
    elif player_choise1.lower() == "ножницы" and player_choise2.lower() == "бумага":
        print("Первый игрок победил!")
    elif player_choise1.lower() == "бумага" and player_choise2.lower() == "ножницы":
        print("Второй игрок победил!")
    else:
        print("Ничья")


def guess_the_number():
    secret_number = int(input("Загадайте число: "))
    while True:
        guess_number = int(input("Отгадайте загаданное число: "))
        if guess_number == secret_number:
            print("Вы угадали!")
            break


def mainMenu():
    print("Игры:")
    print("1. Камень Ножницы Бумага")
    print("2. Угадай число")
    game_choise = int(input("Выберите игру (1 / 2) и нажмите Enter: "))

    if game_choise == 1:
        rock_paper_scissors()
    elif game_choise == 2:
        guess_the_number()
    else:
        print("Неверный ввод.")

mainMenu()
