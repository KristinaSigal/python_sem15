"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака."""


data = {"Спички": 0.3, "Фонарик": 0.5, "Котелок": 1, "Аптечка": 1, "Консервы": 1.5, "Спальник": 1.8,
        "Надувной матрас": 2, "Крупа": 2, "Вода": 3, "Палатка": 3.5, "Лодка": 4}
all_size = float(input("Введите максимальную грузоподъёмность рюкзака в кг.> "))

print(f"Список (вещи : их вес) - {data}")

weight = 0
stock_lst =[]
for key, value in data.items():
    weight += value

if weight > all_size:
    size = all_size
    weight = 0
    for key, value in data.items():
        if value <= size:
            size -= value
            weight += value
            stock_lst.append(key)

    surplus = []
    for elem in data:
        if elem not in stock_lst:
            surplus.append(elem)
    print(f"Поместилось в рюкзак {stock_lst}, общий вес - {weight:.1f}. Не поместилось {surplus}")

else:
    print(f"Вместимость рюкзака ({all_size}) больше общего веса ({weight:.1f}). Ничего не осталось")
