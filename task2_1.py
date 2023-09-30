# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

from math import sqrt

print('Решение квадратного уравнеия вида a*x**2+b*x+c=0')
a = float(input('введите значение a (с учетом знака): '))
b = float(input('введите значение b (с учетом знака): '))
c = float(input('введите значение c (с учетом знака): '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f'"Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
elif d == 0:
    x1 = -b / (2 * a)
    print(f'"Корень уравнения: x = {x1:.3f}')
else:

    real = round(-b / (2 * a), 4)
    imaginary = round(sqrt(abs(d)) / (2 * a), 4)
    x1 = complex(real, imaginary)
    x2 = complex(real, -imaginary)

    print(f'"Корни уравнения: x1 = {x1}; x2 = {x2}')
