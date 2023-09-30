"""
Задача 1
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def my_fun(f_path: str) -> tuple:
    data = full_path.split("\\")
    path = '\\'.join(data[:len(data) - 1:])
    filename = data[len(data) - 1:len(data)]
    name, extension = filename[0].split('.')
    res = path, name, extension
    return res


full_path = "C:\\Users\\Old_Home\\PycharmProjects\\python_semonar_project\\script5_7.py"
print(f'Исходный путь: {full_path} \nКортеж из трех элементов: {my_fun(full_path)}')
