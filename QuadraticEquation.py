import argparse
import logging
from math import sqrt


class QuadraticEquation:
    @staticmethod
    def get_logging(name):
        logging.basicConfig(filename='log\QuadraticEquation.log',
                            filemode='a',
                            encoding='utf-8',
                            format='{levelname:<7} - {asctime} строка {lineno:>3d} : {msg}',
                            style='{',
                            level=logging.INFO)
        return logging.getLogger(name)

    @staticmethod
    def Pars_Equation(args):
        logger = QuadraticEquation.get_logging('parser')

        try:
            a = int(args.a)
        except ValueError as e:
            logger.error(f'коэффициент a:"{args.a}", {e}')

        try:
            b = int(args.b)
        except ValueError as e:
            logger.error(f'коэффициент b:"{args.b}", {e}')

        try:
            c = int(args.c)
        except ValueError as e:
            logger.error(f'коэффициент a:"{args.c}", {e}')

        try:
            equt = QuadraticEquation(a, b, c)
            logger.info(f'Решение уравнения: {a}x^2 + ({b})x + ({c}) = 0 , {equt.Sol_equation()}')
            print(equt.Sol_equation())
        except NameError as e:
            logger.error(f'коэффициенты a:={args.a}, b={args.b}, c={args.c}", ошибка: {e}')
            print('Данные некорректны: Log/quadratic.log')

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def Sol_equation(self):
        d = self.__b ** 2 - 4 * self.__a * self.__c
        if d > 0:
            x1 = (-self.__b + sqrt(d)) / (2 * self.__a)
            x2 = (-self.__b - sqrt(d)) / (2 * self.__a)
            return (f'Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
        elif d == 0:
            x1 = -self.__b / (2 * self.__a)
            return (f'Корень уравнения: x = {x1:.3f}')
        else:
            real = round(-self.__b / (2 * self.__a), 4)
            imaginary = round(sqrt(abs(d)) / (2 * self.__a), 4)
            x1 = complex(real, imaginary)
            x2 = complex(real, -imaginary)
            return (f'Корни уравнения: x1 = {x1}; x2 = {x2}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-a', type=str, default='-5')
    parser.add_argument('-b', type=str, default='5')
    parser.add_argument('-c', type=str, default='0')

    args = parser.parse_args()
    QuadraticEquation.Pars_Equation(args)
