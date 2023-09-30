"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def _leap_year(year):
    if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0:
        return True
    else:
        return False


def check_date(str_data):
    day, month, year = str_data.split(".")
    if int(year) in range(1, 9999 + 1):
        if month in ["01", "03", "05", "07", "08", "10", "12"]:
            if int(day) in range(1, 32):
                return True
            else:
                return False
        elif month != "02":
            if int(day) in range(1, 31):
                return True
            else:
                return False
        else:
            if _leap_year(year):
                if int(day) in range(1, 30):
                    return True
                else:
                    return False
            elif int(day) in range(1, 29):
                return True
            else:
                return False
    else:
        return False


print(check_date("29.02.2024"))
