# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:
# 2 2
#     4

def summa(a, b):
    if a < 0 or b < 0:
        return 'Числа не должны быть отрицательными!'
    if a == 0:
        return b
    else:
        return summa(a-1, b+1)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print(summa(num1, num2))
