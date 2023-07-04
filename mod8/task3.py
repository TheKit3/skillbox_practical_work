reverse_timer = int(input('Введите время приготовления: '))

for sec in range(reverse_timer, -1, -1):
    readiness = (input('Еда готова?'))
    if readiness == 1:
        break

    elif readiness == 0:
        print(sec)

print()
print('Ваша еда готова, осторожно горячo!')
