# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Пример использования:
input_list = [1, 2, 3, 4, 2, 3, 5, 1, 4, 6]
result_list = remove_duplicates(input_list)
print("Результирующий список без дубликатов:", result_list)