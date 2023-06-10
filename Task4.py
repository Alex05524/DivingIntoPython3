# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант

def pack_backpack(items, max_weight):
    sorted_items = sorted(items.items(), key=lambda x: x[1])  # Сортировка вещей по массе
    packed_items = []

    current_weight = 0
    for item, weight in sorted_items:
        if current_weight + weight <= max_weight:
            packed_items.append(item)
            current_weight += weight

    return packed_items

# Пример использования:
items = {
    "Палатка": 2000,
    "Спальник": 1000,
    "Фонарик": 200,
    "Котелок": 500,
    "Коврик": 800,
}

max_weight = 3000

packed_items = pack_backpack(items, max_weight)
print("Вещи, помещенные в рюкзак:")
for item in packed_items:
    print(item)