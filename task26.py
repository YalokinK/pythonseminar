# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# a = int(input('Введите число: '))
# b = int(input('Введите второе число: '))

def multiplic(n, m):
    if n == 1 or m == 1:
        return 1
    return(n**m)
print(multiplic(3, 5))
