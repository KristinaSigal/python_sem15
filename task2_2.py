"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
"""

num = int(input("Введите число, которое хотите преобразовать в шестнадцатеричное: "))
hexadecimal = ""
DIVIDER = 16

print('Проверочное значение:', hex(num))

while num >= 1:
    result = num % DIVIDER
    if result == 10:
        result = 'a'
    elif result == 11:
        result = 'b'
    elif result == 12:
        result = 'c'
    elif result == 13:
        result = 'd'
    elif result == 14:
        result = 'e'
    elif result == 15:
        result = 'f'
    hexadecimal = str(result) + hexadecimal
    num = num // DIVIDER

print('Вычесленное значение:', hexadecimal)
