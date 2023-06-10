# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант
# *Верните все возможные варианты комплектации рюкзака.

def pack_backpack(items, max_weight):
    combinations = []
    current_combination = []

    def backtrack(weight, start_index):
        if weight == 0:
            combinations.append(list(current_combination))
        elif weight < 0:
            return
        else:
            for i in range(start_index, len(items)):
                item, item_weight = items[i]
                current_combination.append(item)
                backtrack(weight - item_weight, i)
                current_combination.pop()

    backtrack(max_weight, 0)
    return combinations

# Пример использования:
items = {
    "Палатка": 2000,
    "Спальник": 1000,
    "Фонарик": 200,
    "Котелок": 500,
    "Коврик": 800,
}

max_weight = 3000

combinations = pack_backpack(items.items(), max_weight)
print("Возможные варианты комплектации рюкзака:")
for combination in combinations:
    print(combination)