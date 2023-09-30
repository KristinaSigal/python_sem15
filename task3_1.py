"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

data = {"Вася": ("Палатка", "Котелок", "Топор", "Шашлык", "Вода"),
        "Петя": ("Палатка", "Котелок", "Топор", "Спички"),
        "Саша": ("Палатка", "Котелок", "Топор", "Консервы"),
        "Коля": ("Палатка", "Котелок", "Спирт", "Вода"),
        }

all_set = set()
for key in data:
    if not all_set:
        all_set = set(data[key])
    else:
        all_set = all_set.intersection(set(data[key]))
print(f'Все три друга взяли:', *all_set)

friends = data.keys()
unc_set = set()
for friend in friends:
    to_remove = set(data[friend])
    one_set = set()
    unc_set = set(data[friend])
    for other_friend in friends:
        if other_friend != friend:
            unc_set = unc_set.difference(set(data[other_friend]))
            if not one_set:
                one_set = set(data[other_friend])
            else:
                one_set = one_set.intersection(set(data[other_friend]))
    one_set -= to_remove

    if unc_set:
        print(f'Уникальные вещи, которые есть только у одного: {friend} -', *unc_set)
    if one_set:
        print(*one_set, f'есть у всех, кроме {friend}')
