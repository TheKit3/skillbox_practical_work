input_string = "Пример строки с символами"
half_length = len(input_string) // 2

new_variable = ""

for i in range(half_length):
    new_variable += input_string[i]

print(new_variable)
