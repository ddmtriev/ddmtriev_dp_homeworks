# print('Лекция №7. Даукша Денис')
# print('\nЗадание №1. Объединение кортежей')
# list1 = [i for i in range(10)]
# tuple1 = tuple(list1)
# print('Кортеж №1: ', tuple1)
# list2 = [i for i in range(10, 20)]
# tuple2 = tuple(list2)
# print('Кортеж №2: ', tuple2)
# tuple3 = tuple1 + tuple2
# print('Результат объеденения кортежей: ', tuple3)

# print('\nЗадание №2. Переобозначить переменные')
# list1 = [i for i in range(10)]
# tuple1 = tuple(list1)
# max_tuple1 = max(tuple1)
# min_tuple1 = min(tuple1)
# max_tuple1, min_tuple1 = min_tuple1, max_tuple1    # Множественное наследование
# print(min_tuple1)
# print(max_tuple1)

# print('\nЗаданеи №3. Добавить пользовательский элемент в список')
# user_number = int(input('Введите элемент, желаемый для добавления в список: '))
# list1 = [i for i in range(10)]
# list1.append(user_number)
# print('Список, полученный в результате: ', list1)

# print('\nЗаданеи №4. Добавить пользовательский элемент в список на указанную позицию')
# user_number = int(input('Введите элемент, желаемый для добавления в список: '))
# list1 = [i for i in range(10)]
# list1.insert(5, user_number)
# print('Список, полученный в результате: ', list1)

# print('\nЗадание №5. Объединение списков в одном.')
# list1 = [i for i in range(10)]
# print('Первый список: ', list1)
# list2 = [i for i in range(10, 20)]
# print('Второй список: ', list2)
# list1.extend(list2)
# print('Результат объединения списков в списке №1: ', list1)

# print('\nЗадание №6. Удалить пользовательский элемент.')
# user_number = int(input('Введите элемент, желаемый для удаления из списка: '))
# list1 = [i for i in range(10)]
# list1.remove(user_number)
# print(list1)

# print('\nЗадание №7. Удалить пользовательский элемент по его позиции.')
# user_number = int(input('Введите позицию элемента, желаемого для удаления из списка: '))
# list1 = [i for i in range(10)]
# list1.remove(list1[user_number])
# print(list1)

# print('\nЗадание №8. Произведение отрицатедбных с нечётными индексами.')
# tuple1 = (-1, 2, -3, -4, 5, 6, -7, -8, 9)
# mult_nums = 1
# for i in tuple1:
#     if i < 0:
#         if tuple1.index(i) % 2 != 0:
#             mult_nums *= i
#     else:
#         continue
# print(mult_nums)

# import random
#
# print('\nЗадание №9. Кортежи рандомнх + нули.')
# list1 = [random.randint(0, 5) for i in range(10)]
# tuple1 = tuple(list1)
# list2 = [random.randint(-5, 0) for i in range(10)]
# tuple2 = tuple(list2)
# tuple3 = tuple1 + tuple2
# num_of_nulls = tuple3.count(0)
# print('Кортеж №3: ', tuple3)
# print('Количество нулей в кортеже №3: ', num_of_nulls)

# print('\nЗадание №10. Вывод без скобок.')
# tuple1 = ('ride', 'slide', 'dipping', 'low')
# print(', '.join(tuple1))

import random

print('\nЗадание №11. Кортежи рандомных + сумма сравнение + мин.')
list1 = [random.randint(10, 90) for i in range(10)]
tuple1 = tuple(list1)
print('Кортеж №1: ', tuple1)
list2 = [random.randint(10, 90) for n in range(10)]
tuple2 = tuple(list2)
print('Кортеж №2: ', tuple2)
sum1 = sum(tuple1)
print('Сумма чисел в первом кортеже = ', sum1)
sum2 = sum(tuple2)
print('Сумма чисел в первом кортеже = ', sum2)
if sum1 > sum2:
    print('Сумма элементов в кортеже 1 больше, чем в кортеже 2')
elif sum1 < sum2:
    print('Сумма элементов в кортеже 2 больше, чем в кортеже 1')
else:
    print('Суммы кортежей равны.')
min1 = min(tuple1)
ind_min1 = tuple1.index(min1)
print('Индекс минимального элемента в первом кортеже:', ind_min1)
min2 = min(tuple2)
ind_min2 = tuple2.index(min2)
print('Индекс минимального элемента во чтором кортеже:', ind_min2)
