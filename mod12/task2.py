def test():
    NumberInQuestion = int(input("Введите число: "))
    if NumberInQuestion > 0:
        positive()

    elif NumberInQuestion < 0:
        negative()

    elif NumberInQuestion == 0:
        print("0")

def positive():
    print("Положительное число.")

def negative():
    print("Отрицательное число.")

test()
