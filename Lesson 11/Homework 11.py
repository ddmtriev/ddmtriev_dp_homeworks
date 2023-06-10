import random
import re    # Для 7. Регулярные выражения.

print('Домашнее задани №12. Даукша Денис.')

print('Задание №1. n + nn + nnn')
input_num = int(input('Введите число n: '))
try:
    if input_num in range(0, 10):
        result = input_num + int(str(input_num)*2) + int(str(input_num)*3)
except ValueError:
    print('Ошибка. Повторите ввод.')
else:
    print(result)
finally:
    print('Завершение программы.')

print('Задание №2. Сон.')
a_hours = int(input('Введите минимальное количество часов сна: '))
b_hours = int(input('Введите максимальное количество часов сна: '))
h_hours = int(input('Введите Ваше актуальное количество часов сна: '))
try:
    if (h_hours >= a_hours) and (h_hours <= b_hours):
        print('Это нормальное количество часов сна.')
    elif h_hours < a_hours:
        print('Беда. Это недосып!')
    else:
        print('Карамба! Это пересып. Проснись и пой!!!')
except ValueError:
    print('Ошибка. Повторите ввод.')
finally:
    print('Завершение программы.')

print('Задание №3. Умножить элементы списка на -2.')
list1 = [random.randint(0,10) for i in range(5)]
print(f'Исходный список: {list1}')
for i in list1:
    i *= -2
    list2.append(i)
print(f'Новый список, где элементы умножены на -2: {list2}')

print('Задание №4. Посчитать количество положительных чисел в списке.')
list_of_nums = [random.randint(-10, 10) for i in range(3)]
print('Исходный список: ', list_of_nums)
pos_count = 0
for i in list_of_nums:
    if i > 0:
        pos_count += 1
print('Количество положительных чисел в исходном списке = ', pos_count)

print('Задание №5. Сгенерировать список. Перевести в строку.')
list1 = [f'{random.randrange(10)}' for i in range(10)]
print(list1)
list1 = ' '.join(list1)
print(list1)

print('Задание №6. Даны два словаря. Объеденить в один.')
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)
dictionary_3 = {**dictionary_1, **dictionary_2}
print(dictionary_3)

print('Задания №7. Удалить знаки припинания из строки.')
input_string = input('Введите строку со знаками припинания. Ответ: ')
print('Исходная строка: ', input_string)
new_string = re.sub(r'[^\w\s]', '', input_string)   # Метод sub заменяет совпадения. [^\w\s] - всё, кроме букв, \
# цифр, пробелов. => паттерн.
print('Новая строка: ', new_string)

print('Задание №8. Сортировка слов в строке в алфавитном порядке.')
input_string = input('Введите строку со знаками припинания. Ответ: ')
print('Исходная строка: ', input_string)
list_from_string = input_string.split(' ')
sortd_string = ' '.join(sorted(list_from_string))
print('Отсортированная строка', sortd_string)