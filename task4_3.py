"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
- Разбейте её на отдельные операции — функции.
- Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

from datetime import datetime

summ = 0
count = 0
percent_out = 0.015
percent_add = 0.03
percent_rich = 0.1
rich_summ = 5000000
min_tax = 30
max_tax = 600

def add_cash(cash: float) -> None:
    global summ
    global count
    summ += cash
    count += 1


def out_cash(cash: float) -> None:
    global summ
    global count
    summ -= cash
    count += 1
    comission = cash * percent_out
    if comission < min_tax:
        comission = min_tax
    elif comission > max_tax:
        comission = max_tax
    summ -= comission
    print(f'списаны проценты за снятие: {comission}')


def check_cash() -> int:
    while True:
        cash = int(input('Введите сумму операции кратную 50\n:> '))
        if cash % 50 == 0:
            return cash
        else:
            print('Введена некорректная сумма (некратна 50)')


def add_percent():
    global summ
    print(f'начислены проценты в размере: {percent_add * summ:.2f}')
    summ = summ + percent_add * summ


log_operation = []

while True:
    action = input('O - снять деньги\nA - пополнить\nH - вывести историю операций\nQ - выйти\n:> ').lower()
    if summ > rich_summ:
        tax = summ * percent_rich
        summ -= tax
        log_operation.append([str(datetime.now()), "удержан налог на богатсво", -tax])
        print(f'списан налог на богатство: {tax}')
    if action == 'o':
        cash = check_cash()
        if cash < summ:
            out_cash(cash)
            log_operation.append([str(datetime.now()), "снятие наличных", -cash])
        else:
            print('недостаточно средств\n')
    elif action == 'a':
        cash = check_cash()
        add_cash(cash)
        log_operation.append([str(datetime.now()), "внесение наличных", cash])
    elif action == 'h':
        print('история операций:')
        print(log_operation)
    elif action == 'q':
        print('Выход из банкомата')
        exit()
    else:
        print('Ошибка ввода. Пожалуйста, повторите ввод')

    if count % 3 == 0:
        add_percent()

    print(f'Текущий баланс = {summ:.2f}')
