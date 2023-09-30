"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv
from task6_1 import check_date


str_data = argv[1]
print(check_date(str_data))
