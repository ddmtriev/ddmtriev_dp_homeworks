import random

print('Домашнее задание №10. Даукша Денис')

print('\nЗадание №1. Действия над словарём.')    # ) Создать произвольный словарь \
# 2. Добавить новый элемент с ключом типа str и значением типа int
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list) 4. Получить элемент по ключу \
# 5. Удалить элемент по ключу 6. Получить список ключей словаря.
input_dict = {random.randint(0, 10): random.randint(0, 100) for dict_elem in range(random.randint(0, 10))}
print(input_dict)
input_dict['Hello'] = 13
print(input_dict)
input_tuple = tuple(random.randint(0, 5) for tuple_elem in range(5))
input_list = [random.randint(0, 10) for list_elem in range(5)]
print(input_tuple)
print(input_list)
new_input_dict = {input_tuple: input_list}
print(new_input_dict)
input_dict.update(new_input_dict)
print(input_dict)
print(input_dict.get('Hello'))
del input_dict['Hello']
print(input_dict)
print(input_dict.keys())

print('\nЗадание №2. Множества. Операции над множествами.')    # Создать множество. Создать неизменяемое множество. \
# Выполнить операцию объединения созданных множеств. Выполнить операцию пересечения созданных множеств.

# Задание множества.
set1 = {1, 3, 5, 7, 9}
print(set1)
set2 = set([1, 3, 5, 7, 9])
print(set2)
set3 = frozenset([2, 4, 5, 6, 7])
print(set3)

# Объединение.
set4 = set1.union(set3)
print(set4)
set2.update(set3)
print(set2)
# Пересечение.
print('Пересечение множеств: ', set1.intersection(set3))

print('\nЗадание №3. Нужно вернуть список, который состоит из элементов, общих для этих двух списков.')
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('Список 1:', list1)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print('Список 2:', list2)
set1 = set(list1)
set2 = set(list2)
print('Список состоящий из общих элементов для обоих списков: ', list(set1.intersection(set2)))

print('\nЗадание №4. Строка. Сохранить в ней только первые вхождения символов. Вывод - кортеж')
input_string = input('Введите строку. Ответ: ')
print('Исходная строка: ', input_string)
input_set = set(input_string)
print('Элементы исходной строки без дубликатов: ', tuple(input_set))

print('\nЗадание №5. 2 множества. Состоит. Пересечение.')
set1 = set(input('Введите первое множество.(Подряд: пр.123). Ответ:'))
print(set1)
set2 = set(input('Введите второе множество.(Подряд: пр.123). Ответ:'))
print(set2)
if set1 == set2:
    print('Заданные множества равны.')
elif set1.issubset(set2):
    print('Множество 1 полностью состоит из элементов множества 2.')
elif set2.issubset(set1):
    print('Множество 2 полностью состоит из элементов множества 1.')
else:
    print('Множества независимы друг от друга.')
bool_intersect = bool(set1.intersection(set2))
if bool_intersect:
    print('Множества пересекаются в: ', set1.intersection(set2))
else:
    print('Множества не пересекаются.')
