# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def summa(n, m):
    if m < 0 or n < 0:
        return - 1
    return n+m

print(summa(2, 2))
