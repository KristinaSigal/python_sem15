# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.
import fractions

## Вариант 2 (с учетом возможного сокращения дробей)
def calculate_gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            _gcd = i
    return _gcd


fract_1 = input("Введите первую дробь в виде a/b: ").split("/")
fract_2 = input("Введите вторую дробь в виде с/d: ").split("/")

# sum_of_fractions
common_denominator = int(fract_1[1]) * int(fract_2[1])
a = int(fract_1[0]) * common_denominator / int(fract_1[1]) + int(fract_2[0]) * common_denominator / int(fract_2[1])
calc_gcd = calculate_gcd(int(a), common_denominator)
sum_of_fractions = f"{int(a / calc_gcd)}/{int(common_denominator / calc_gcd)}"

# product_of_fractions
numer = int(fract_1[0]) * int(fract_2[0])
den = int(fract_1[1]) * int(fract_2[1])
calc_gcd = calculate_gcd(numer, den)
product_of_fractions = f"{int(numer / calc_gcd)}/{int(den / calc_gcd)}"

print(f"Результат сложение дробей: {fract_1[0]}/{fract_1[1]} + {fract_2[0]}/{fract_2[1]} = {sum_of_fractions}")
print(f"Результат произведение дробей: {fract_1[0]}/{fract_1[1]} * {fract_2[0]}/{fract_2[1]} = {product_of_fractions}")


print("\nПроверка при помощи <fractions>")
f1 = fractions.Fraction(int(fract_1[0]), int(fract_1[1]))
f2 = fractions.Fraction(int(fract_2[0]), int(fract_2[1]))
print(f"сложение => {f1 + f2}")
print(f"произведение => {f1 * f2}")
