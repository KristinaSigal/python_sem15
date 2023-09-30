import logging
import argparse

#logging.basicConfig(level='DEBUG')

class Rectangle:
    __slots__ = ('__l', '__w', '__selfRectNum', '__logger')

    rectNumber = 0
    @staticmethod
    def inc_rectNum():
        Rectangle.rectNumber = Rectangle.rectNumber+1
    @staticmethod
    def set_logging():
        logging.basicConfig(filename='log\Rectangle.log',
                            filemode='a',
                            encoding='utf-8',
                            format='{levelname:<7} - {asctime} строка {lineno:>3d} : {msg}',
                            style='{',
                            level=logging.INFO)


    @staticmethod
    def pars_args (args):

        try:
            l1 = int(args.l1)
        except ValueError as e:
            l1 = -1

        try:
            w1 = int(args.w1)
        except ValueError as e:
            w1 = -1

        try:
            l2 = int(args.l2)
        except ValueError as e:
            l2 = -1

        try:
            w2 = int(args.w2)
        except ValueError as e:
            w2 = -1

        r1 = Rectangle(l1, w1)
        r2 = Rectangle(l2,w2)
        Rectangle.operation(r1,r2 , args.operation)


    @staticmethod
    def operation(rectangle1, rectangle2, op):

        Rectangle.set_logging()
        logger = logging.getLogger('peration')
        if op == "=":
            print(rectangle1 == rectangle2)
            logger.info(f'Проверка == : {(rectangle1 == rectangle2)}')
        elif op == ">":
            print(rectangle1 > rectangle2)
            logger.info(f'Проверка >: {(rectangle1 > rectangle2)}')
        elif op == "<":
            print(rectangle1 < rectangle2)
            logger.info(f'Проверка <: {(rectangle1 < rectangle2)}')
        elif op == "+":
            rectangle3 = rectangle1 + rectangle2
            logger.info(f'Сложение: {rectangle3}')
            print(rectangle3)
        elif op == "-":
            rectangle3 = rectangle2 - rectangle1
            logger.info(f'Вычитание: {rectangle3}')
            print(rectangle3)
        else:
            logger.info(f'Error: {op}')
            print(f'Передена некорректная операция: {op}')


    def __init__(self, length, width = 0):
        if length > 0 and width >= 0:
            Rectangle.set_logging()
            Rectangle.inc_rectNum()
            self.__selfRectNum = Rectangle.rectNumber
            self.__l = length
            self.__logger = logging.getLogger(f'Rectangle_{Rectangle.rectNumber}')
            if width != 0:
                self.__w = width
            else:
                self.__w = self.__l
            self.__logger.info(f'Создание прямоугольника {self.__l}х{self.__w} ')
        else:
            raise Exception("Длинна и ширина должны быть положительными.")

    def prn(self):
        print(f'{self.__l} x {self.__w}')

    @property
    def width(self):
        return self.__w

    @property
    def length(self):
        return self.__l

    def get_perimeter(self):
        return 2 * (self.__w + self.__l)

    def get_square(self):
        self.__logger.info (f'вычисление площади ')
        return self.__w * self.__l

    def __add__(self, other):
        self.__logger.info(f'сложение')
        return Rectangle(other.length+self.length, other.width + self.width,)

    def __sub__(self, other):
        self.__logger.info(f'вычитание')
        return Rectangle(self.length-other.length, self.width-other.width)

    def __eq__(self, other):
        self.__logger.info(f'проверка эквивалентности ')
        return self.get_square() == other.get_square()

    def __ne__(self, other):
        self.__logger.info(f'проверка на равенства')
        return self.get_square() != other.get_square()

    def __gt__(self, other):  # больше >
        self.__logger.info(f'больше')
        return self.get_square() > other.get_square()

    def __ge__(self, other):  # больше или равно >=
        self.__logger.info(f'больше или равно ')
        return self.get_square() >= other.get_square()

    def __lt__(self, other):  # метод меньше <
        self.__logger.info(f'меньше')
        return self.get_square() < other.get_square()

    def __le__(self, other):  # меньше или равно <=
        self.__logger.info(f'меньше или равно ')
        return self.get_square() <= other.get_square()

    def __str__(self):
        return f'Прямоугольник  {self.length} X {self.width}'

    def print_num(self):
        print(f'Rectangle_{self.__selfRectNum }')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-l1', type=str, default='1')
    parser.add_argument('-w1', type=str, default='2')
    parser.add_argument('-l2', type=str, default='3')
    parser.add_argument('-w2', type=str, default='4')
    parser.add_argument('-operation', type=str, default='=')

    Rectangle.pars_args(parser.parse_args())



