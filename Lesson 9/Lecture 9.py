import random

print('Лекция №9. Даукша Денис')

# print('Задание №1. Исправить => True')
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1["b"] == d2["b"])

# print('\nЗадание №2. Словарь с числами. Все перемножить.')
# dict1 = {random.randint(1, 10): random.randint(1, 10) for i in range(10)}    # От еденицы, чтобы произведение не занулялось.
# print(f'Исходный словарь: {dict1}')
# val_mult = 1
# val_list = []
# for nums in dict1:
#     val_list.append(dict1[nums])
#     val_mult *= dict1[nums]
# print(f'Список значений словаря: {val_list}')
# print(f'Произведение значений словаря = {val_mult}')

# print('\nЗадание №3. Два списка одинаковой длины. Словарь: {Спис1: Спис2, ...}')
# list1 = [i for i in range(1, 5 + 1)]
# print(f'Список №1: {list1}')
# list2 = [random.randint(0, 10) for i in range(5)]
# print(f'Список №2: {list2}')
# dict1 = dict(zip(list1, list2))
# print(f'Результат объединения списков: {dict1}')

# print('\nЗадание №4. Pythonist => {i: repeat_num}')
# name = 'pythonist'
# list1 = list(name)
# list2 = []
# # print(list1)
# for i in list1:
#     repeat_num = list1.count(i)
#     # print(f'{i}: {repeat_num}')
#     list2.append(repeat_num)
#     dict1 = dict(zip(list1, list2))
# print(dict1)

# print('\nЗадание №5. Добавить каждому ключу число равное длине этого ключа')
# dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# keys = dict1.keys()
# keys_list = []
# for keys in dict1:
#     key_len = str(len(keys))
#     keys = keys + key_len
#     keys_list.append(keys)
# print(dict(zip(keys_list, dict1.values())))

# print('\nЗадане №6. Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.')
# keys = [random.randint(1,10) for i in range(10)]
# vals = []
# for i in keys:
#     val = i ** 3
#     vals.append(val)
# dict1 = dict(zip(keys, vals))
# print(dict1)

# print('\nЗадание №7. Три способа задания словаря.')
# dict1 = {'1': 0, '2': 0, '3': 0}
# print(dict1)
# dict2 = {f'{i}': 0 for i in range(1, 3 + 1)}
# print(dict2)
# dict3 = dict.fromkeys(['1', '2', '3'], 0)
# print(dict3)
# dict4 = dict(zip(['1', '2', '3'], [0, 0, 0]))
# print(dict4)

print('\n 8')
list1 = [random.randint(0,10) for i in range(10)]
print(list1)
set1 = set(list1)
if len(list1) != len(set1):
    print('В исходной последовательности есть дубликаты.')
    print(f'Последовательность без дубликатов: {set1}')
else:
    print('Дубликатов в исходной последовательности нет.')

print('\n 9')

print('\n 10')

print('\n 11')

