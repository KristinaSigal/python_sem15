"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [1, 2, 1, 1, 2, 3, 4, 5, 5, 'row', 'not', 'row']

new_lst = []
for elem in lst:
    if lst.count(elem) > 1:
        new_lst.append(elem)
print(list(set(new_lst)))

#list comprehension
print(list(set(elem for elem in lst if lst.count(elem) > 1)))