# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
n = int (input ('Введите длину списка: '))
for k in range (1, n+1):
    num2 = 0
    num2 = round((1 + 1/k) ** k, 3)
    num_list.append(num2)

print(f'{num_list} \n Сумма: {round(sum(num_list), 3)}')
