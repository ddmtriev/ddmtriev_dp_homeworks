import os    # Для №1
import random    # Для №2,6
import math    # Для 8


print('Самостоятельная работа №2. Даукша Денис.')

print('\nЗадание №1. Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, \
test_3.txt.	Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt. После этого удалите созданную папку.\
 Все операции выполнять с помощью встроенных функций библиотеки os.')

os.mkdir(r'C:\Users\user\Desktop\Task_1')    # Создание папки

os.chdir(r'C:\Users\user\Desktop\Task_1')    # Перемещение в папку
with open('test_1.txt', 'w') as f1:    # Создпние файла в папке
    f1.write('Это файл тест 1')    # Запись данных в файл
with open('test_2.txt', 'w') as f2:
    f2.write('Это файл тест 2')
with open('test_3.txt', 'w') as f3:
    f3.write('Это файл тест 3')

os.rename('test_1.txt', 'rename_1.txt')    # Переименование файлов в папке
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')

os.remove(r'C:\Users\user\Desktop\Task_1\rename_1.txt')    # Удаление файлов из папки
os.remove(r'C:\Users\user\Desktop\Task_1\rename_2.txt')
os.remove(r'C:\Users\user\Desktop\Task_1\rename_3.txt')
os.chdir('..')    # Выход из папки
os.rmdir(r'C:\Users\user\Desktop\Task_1')    # Удаление папки

print('\nЗадание №2. Найти в списке те элементы, значение которых меньше среднего арифметического, \
взятого от всех элементов списка.')

input_list = [random.randint(0, 10) for elem in range(10)]    # Генерируем случайный список
new_list = []    # Пустой список для заполнения отсортированными значниями
print(f'Исходный список: {input_list}')
param = sum(input_list)/len(input_list)    # Считаем среднее арифметическое - параметр
print(f'Среднее арифметическое: {param}')
for elem in input_list:
    if elem < param:
        new_list.append(elem)    # Добавляем элементы, удовлетворяющие условию в новый список
print(f'Элементы списка, которые меньше, чем среднее арифметическое: {new_list}')

print('\nЗадание №3. Создайте словарь из строки " An apple a day keeps the doctor away " следующим образом: \
в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений \
данной буквы в строку.')

input_string = 'An apple a day keeps the doctor away'
for elem in input_string:
    convert_dict = {f'{elem}': input_string.count(elem) for elem in input_string}    # (Не совсем)Функция преобразования
print(f'Результат преобразования исходной строки: {convert_dict}')

print('\nЗадание №4. Ввести 10 чисел с клавиатуры, данные числа добавить во множество.')

input_set = (input('Введите 10 чисел. (Через пробел). Ответ: ')).split(' ')    # Конвертируем строку в список \
# методом .split()
input_set = set(input_set)    # Конвертируем список во множество
print(f'input set - это {type(input_set)} и содержит: \n{input_set}')

print("\nЗадание №5. Есть словарь песен группы Depeche Mode violator songsdict = { 'World in My Eyes': 4.76, \
'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, \
'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, } \
Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых больше 5 минут \
Создайте новый словарь тех песен, в название которых состоит из одного слова")

sn_dict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
           'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18,
           'Clean': 5.68, }
duration = 0
more_5_dur = []
one_w_key_dict = {}
for keys in sn_dict:
    duration += sn_dict[keys]    # Вызываем значения и суммируем их
    if sn_dict[keys] > 5:    # Проверяем значения больше 5-и и вызываем их ключи в список
        more_5_dur.append(keys)
    if keys.count(' ') == 0:    # ПРоверяем наличие ' ' в ключе
        one_w_pair = {keys: sn_dict.get(keys)}    # Создаем словарь по найденному совпадению
        one_w_key_dict.update(one_w_pair)    # Обновляем в случае нового совпадения

print(f'\nОбщее время звучания всех песен: {duration} мин. Песни, длительность которых более 5-и минут: {more_5_dur}.'
      f'Словарь песен, названия которых состоят из одного слова: {one_w_key_dict}')

print('\nЗадание №6. Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b]. \
Освободившиеся в конце массива элементы заполнить нулями.')

input_list = [random.randint(0, 10) for elem in range(10)]
print(f'Исходный список: {input_list}')
a = int(input('Введите первое число интервала - a: '))
b = int(input('Введите второе число интервала - b: '))
new_list = [elem for elem in input_list if (elem < a) or (elem > b)]    # Создал список из невходящих в интервал эл-ов
print(f'Сжатый список: {new_list}')
while len(new_list) < len(input_list):
    new_list.append(0)    # Заполняем сжатый массив 0-ями до тех пор пока длина не сравняется с исходной
print(f'Список, после заполнения освободившихся в конце массива элементов нулями: {new_list}')

print('\nЗадание №7. Ввести строку. Вывести на экран букву, которая находится в середине этой строки. \
Также, если эта центральная буква равна первой букве в строке, то создать и вывести часть строки между первым и \
последним символами исходной строки. (подсказка: для получения центральной буквы, найдите длину строки и разделите \
ее пополам. Для создания результирующий строки используйте срез)')

input_string = input('\nВведите строку. Ответ: ')
midd_index = len(input_string) // 2
print(f'Элемент, находящийся в середине строки: {input_string[midd_index]}')
if input_string[0] == input_string[midd_index]:
    print(f'Часть строки, между первым и последним символами{input_string[1:-1]}')

print('\nЗадание №8. Напишите программу, которая подключает модуль math и, используя значение числа \pi  \
из этого модуля, вводим радиус круга  и находим периметр этого круга, результат вывести на экран.')


def calculate(r):    # Функция для рассчёта длины(периметра) окружности(круга)
    circ_length = 2 * math.pi * r
    return f'Длина окружности = {circ_length}'


circ_radius = float(input('Введите радиус круга(Окружности). Ответ: '))
print(calculate(circ_radius))

print('\nЗадание №9. Джайден Смит. Каждое слово с большой буквы.')
input_string = input('Введите строку. Ответ: ')
string_to_list = input_string.split(' ')
result_string = ' '.join([elem.capitalize() for elem in string_to_list])     # Преобразуем элементы в списке \
# string_to_list, создавая новый список с помощью генератора и сразу же разворачиваем его в строку методом .join()
print(result_string)

print('\nЗадание №10. Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]. Необходимо вывести элементы, \
которые одновременно 1) меньше 30 и 2) делятся на 3 без остатка. Все остальные элементы списка необходимо \
просуммировать и вывести конечный результат.')

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst1 = ' '.join(map(str, [elem for elem in lst if (elem < 30) and (elem % 3 == 0)]))     # Создал список lst1 >> \
# 1-ый параметр >> преобразование в строку для вывода
print(f'Элементы, которые меньше 30 и делятся на 3 без остатка: {lst1}')
lst1 = [elem for elem in lst if (elem < 30) and (elem % 3 == 0)]     # Дубль lst1 для работы со вторым генератором
lst2 = [elem for elem in lst if elem not in lst1]    # Второй генератор >> параметр-остальное
print('Сумма остальных элементов: ', sum(lst2))

print('\nЗадание №11. Создайте список [ 18, 14, 10, 6, 2 ]  с помощью функции range()')
result_list = [elem for elem in range(18, 1, -4)]    # Генератор списка с элементами в диапазоне от 18 до 1 с шагом -4
print(result_list)