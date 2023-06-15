import random    # №13
import math

print('Самостоятельная работа №1. Даукша Денис.')

print('\nЗадание №1. Самое большое число из цифр 4, 4, 4. Его значение.')    # Используюя стандартные математические \
# операции представить самое большое целое число из цифр 4, 4, 4.
largest_number = (4 * 4) ** 4
print(f'Самое большое целое число из цифр 4, 4, 4: {largest_number}')

print('\nЗадание №2. Вычислить значение выражения.')
x = 2
y = 3
z = 4
c = (1/4)*(math.sin(x + y - z) + math.sin(y + z - x) + math.sin(z + x - y) - math.sin(x + z + y))
print('Ответ: ', c, 'Рад.')

print('\nЗадание №3. Пустая переменная. Проверка истина/ложь. Объяснение.')    # Создать пустую переменную проверить \
# её на истинность, результат объяснить.
x = bool('')
print(f'Результат проверки истинности пустой перемнной x: {x}')
print('Обяснение. Результат False т.к. пустая переменная это 0. Не пустая переменная это 1. \
А, как мы знаем, 0 = False, 1 = True.')

print('\nЗадание №4. m<=n. Вывести все числа от m до n включительно.')    # Даны два числа м и н, м <= н, вывести \
# все числа от м до н включительно.
m = int(input('Введите число m. Ответ: '))
n = int(input('Введите число n, которое будет >= m. Ответ: '))
if n < m:
    print('Ошибка. Число n должно быть больше числа m.')
elif m == n:
    print('Введённые числа равны.')
else:
    for i in range(m, n+1):
        print(i)

print('\nЗадание №5. m и n. Порядок вывода в зависимости от того, какое больше.')    # В порядке возрастания, \
# если m<n, или в порядке убывания в противном случае.
m = int(input('Введите число m. Ответ: '))
n = int(input('Введите число n. Ответ: '))
if m < n:
    print('\nТ.к. число n больше числа m: ввод в порядке возрастания.')
    for i in range(m, n+1):
        print(i)
elif m == n:
    print('Введённые числа равны.')
else:
    print('\nТ.к. число m больше числа n: ввод в порядке убывания.')
    for i in range(m, n-1, -1):
        print(i)

print('\nЗадание №6. Имя фамилия => фамилия имя.')
name = input('Введите Ваше имя. Ответ: ')
surname = input('Введите Вашу фамилию. Ответ: ')
user_id = name + ' ' + surname
print(f'Имя, фамилия: {user_id}')
name, surname = surname, name
user_id1 = name + ' ' + surname
print(f'Фамилия, имя: {user_id1}')

print('\nЗадание №7. Список с числами от 1 до 50 используя генератор списков.')
nums = [i for i in range(1, 50+1)]
print(f'Список с числами от 1 до 50: {nums}')

print('\nЗадание №8. Найти, какое число не имеет пары.')
nums = [1, 5, 2, 9, 2, 9, 1]
list_non_pairs = []
for i in nums:
    if nums.count(i) != 2:
        list_non_pairs.append(i)
print(f'Исходный список: {nums}. Число, не имеющее пары: {list_non_pairs}')

print('\nЗадание №9. Добавить слово к каждому элементу списка.')
list1 = ['student1', 'student2', 'student3']
print(f'Исходный список: {list1}')
list2 = []
for student in list1:
    i = student + '_good'
    list2.append(i)
print(f'Новый список: {list2}')

print('\nЗадание №10. Вывести на экран числа от 0 до 50, кроме 35.')
for i in range(1, 50+1):
    if i != 35:
        print(i)
    else:
        continue

print('\nЗадание №11. Исходная строка. Добавить элементы, где есть ' ' в новый список.')
list1 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
print(f'Исходный список: {list1}')
list2 = []
for sent in list1:    # Разбил список1 на элемнты для проверки каждого
    x = bool(' ' in sent)    # Ввёл булевую переменную, по которой можно определить наличие ' ' в элементе списка
    # print(x)    # Для проверки
    if x == 1:    # Если булевая переменаая возвращает True - выполнить
        list2.append(sent)    # Добавить элемент в список
print(f'Новый список: {list2}')

print('\nЗадание №12. Первый/второй для школьников.')
pupils_num = int(input('Введите кол-во человек в классе. Ответ: '))
for i in range(1, pupils_num + 1):
    if i % 2 != 0:
        print(f'Ученик {i}: Первый!')
    else:
        print(f'Ученик {i}: Второй!')

print('\nЗадание №13. Список чисел. Удалить из него все 20-ки.')
list1 = [random.randint(1, 20) for i in range(10)]
list1.insert(5, 20)    # На всякий случай. Чтобы в списке всегда было что удалять \
# вне зависимости от сгенерированных значений
print(f'Исходный список: {list1}')
for i in list1:
    if i == 20:
        list1.remove(i)
print(f'Список в котором исключено число 20: {list1}')

print('\nЗадание №14. Вывести все чётные из 10-и значного числа.')
num = list(input('Введите 10-и значное число. Ответ: '))
num_len = len(num)
list2 = []
for i in num:
    if num_len != 10:
        print('Ошибка. Вы ввели НЕ 10-и значное число. Повторите попытку.')
        exit()
    elif int(i) % 2 == 0:
        list2.append(i)
print(f'Чётные числа в числе: {list2}')

print('\nЗадание №15. Удалить пустые строки  из списка строк.')
st1 = input('Введите строку №1. (Пустая строка допустима). Ответ: ')
st2 = input('Введите строку №1. (Пустая строка допустима). Ответ: ')
st3 = input('Введите строку №1. (Пустая строка допустима). Ответ: ')
st4 = input('Введите строку №1. (Пустая строка допустима). Ответ: ')
st5 = input('Введите строку №1. (Пустая строка допустима). Ответ: ')
list1 = [st1, st2, st3, st4, st5]
print(f'Исходный список: {list1}')
for st in list1:
    if st == '':
        list1.remove(st)
print(f'Список1 без пустых строк: {list1}')

print('\nЗадание №16. Процентное содержание G и C в коде ДНК.')
dnk_code = input('Введите код цепочки ДНК. Ответ: ')
dnk_code = dnk_code.lower()
dnk_code = dnk_code.strip()
# print(dnk_code)
c_code = dnk_code.count('c')
# print(c_code)
g_code = dnk_code.count('g')
# print(g_code)
code_len = len(dnk_code)
# print(code_len)
percentage = ((c_code + g_code)/code_len)*100
print(f'Процентное содержание G и C нуклеотидов в цепочке ДНК: {percentage}%')

print('\nЗадание №17. Исходный код ДНК. Вывести соответсующую ему комплементарную цепь.')
dnk_code = input('Введите код цепочки ДНК. Ответ: ')
print(dnk_code)
dnk_code = dnk_code.upper()
comp_dnk_code = ''
for i in dnk_code:
    if i == 'A':
        comp_dnk_code += 'T'
    elif i == 'T':
        comp_dnk_code += 'A'
    elif i == 'C':
        comp_dnk_code += 'G'
    elif i == 'G':
        comp_dnk_code += 'C'
print(f'Исходный код => комплементарный код: {dnk_code} => {comp_dnk_code}')
