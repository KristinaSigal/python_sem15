"""
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление. .

"""


def swap_kwargs(**kwargs):
    result = {}
    # print(kwargs)
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


res = swap_kwargs(fist_name='Sergey', last_name='Terekhin', summer_months=['June', 'July', 'August'],
                  my_dict={'Immersion_python': 'Homework 4', 'Homework 4': 'task 2'})
print(res)
