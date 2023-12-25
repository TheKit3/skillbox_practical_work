def summa_n():
    N = int(input("Введите число: "))
    SumOfNumbers = 0

    for i in range(N+1):
        SumOfNumbers += i
        #print(SumOfNumbers)

    print("Я знаю, что сумма чисел от 1 до", N, "равна", SumOfNumbers)

summa_n()
