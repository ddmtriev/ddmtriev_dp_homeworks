from collections import Counter    # Для 5

print('Домашнее задание №9. Даукша Денис.')

print('\nЗадание №1. }. Объедините два словаря в один при помощи встроенных функций языка Python.')
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)
dictionary_3 = {**dictionary_1, **dictionary_2}
print(dictionary_3)

print('\nЗадание №2. Три способа задания словаря.')
dict1 = {'1': 0, '2': 0, '3': 0}
print(dict1)
dict2 = {f'{i}': 0 for i in range(1, 3 + 1)}
print(dict2)
dict3 = dict.fromkeys(['1', '2', '3'], 0)
print(dict3)

print('\nЗадание №3. Новый список. "_" заменить на " "')
list1 = ['ab_cd_e', 'abc', 'a_b_c', 'a__bc_d_', '__']
print(f'Исходный список: {list1}')
list2 = []
for i in list1:
    if '_' in i:
        list2.append(i.replace('_', ' '))
print(f'Новый список: {list2}')

print('\nЗадание №4. Словарь. Список произведений Ключ * Значение.')
dict1 = {1: 10, 2: 20, 3: 30}
print(f'Исходный словарь: {dict1}')
res_list = []
for i in dict1:
    mult = i * dict1[i]
    res_list.append(mult)
print(f'Список произведений (Ключ * Значение): {res_list}')

print('\nЗадание №5. Статистика частности букв в кортеже.')
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(f'Исходный кортеж: {long_word}')
count_elem = dict(Counter(long_word))
print(f'Число повторений элементов(i: n): {count_elem}')
