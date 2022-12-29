# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.


def lens_number(x: float) -> int:
    len_number = 0
    norm_number = 0
    string_number = str(x)
    len_number = len(string_number)
    norm_number = x * (10 ** (len_number-2))
    return norm_number

def sum_all_number(x: int) -> int:
    d = []
    summ_all = 0
    while x > 0:
        d.append(x % 10)
        x = x//10
    for i in d:
        summ_all = summ_all + i
    return summ_all

x = float(input('Введите число: '))
lens_number(x)
print(int(sum_all_number(lens_number(x))))
