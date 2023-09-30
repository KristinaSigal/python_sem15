data = {"Палатка": 3.5, "Лодка надувная": 4, "Котелок": 1, "Аптечка": 1, "Консервы": 1.5,
        "Спальник": 1.8, "Крупа": 2, "Спички": 0.3, "Фонарик": 0.5, "Вода": 3}

max_size = float(input("Введите максимальную грузоподъёмность рюкзака в кг.> "))
# определяем вещь с минимальным весом
data = dict(sorted(data.items(), key=lambda item: item[1]))
first_key = list(data.keys())[0]
MIN_W = data[first_key]
# напонения рюкзака начнем с наиболее тяжелых вещей
data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print(f"Несколько вариантов максимально возможного наполнения рюкзака, исходя из вместимости {max_size} кг:")
weight = 0
stock_lst = []
for key, value in data.items():
    weight += value
if weight > max_size:
    count = 0
    for key, value in data.items():
        size = max_size
        stock_lst = []
        weight = 0
        stock_lst.append(key)
        size -= value
        weight += value
        for key_1, value_1 in data.items():
            if value_1 <= size:
                if key != key_1:
                    size -= value_1
                    weight += value_1
                    stock_lst.append(key_1)
            elif size > MIN_W:
                continue
            else:
                count += 1
                surplus = []
                for elem in data:
                    if elem not in stock_lst:
                        surplus.append(elem)
                print(f"{count}) Поместилось в рюкзак {stock_lst}, общий вес - {weight:.1f}. Не поместилось {surplus}")
                break
else:
    print(f"Все вещи вместились. Вместимость рюкзака ({max_size}) больше общего веса ({weight:.1f}).")
