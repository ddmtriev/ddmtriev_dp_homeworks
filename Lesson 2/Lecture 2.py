import random

print('Лекция №2. Даукша Денис')
print('\nЗадание №1')
str1 = "Hello my name is"    # Вывести my name, наоборот, ll, Hello is
print(str1[6:13])
print(str1[::-1])
print(str1[2:4])
print(str1[0:6], str1[-2:])

print('\nЗадание №2. Работа с именем.')    # Hello, ...; Name * 3
name = input('Введите Ваше имя. Ответ: ')
print('Привет,', name)
print(name * 3)

print('\nЗадание №3. Сумма чисел случайного трёхзначного числа.')    # Решить через строки.
num1 = random.randint(100,999)
num1 = str(num1)
print(num1)
a1 = int(num1[0])
a2 = int(num1[1])
a3 = int(num1[2])
num1 = a1 + a2 + a3
print(num1)

print('\nЗадание №4. Непустая строка на входе.')
str1 = input('Введите строку (Минимум 2 символа). Ответ:')
if len(str1) < 2:
    print('Ошибка. Недостаточно символов в строке.')
    exit()
else:
    str3 = str1[0::3]    # Каждый 3-ий символ, начиная с нуля. Без пробелов.
    print('Каждый 3 символ:', str3.replace(' ', ''))
    str2 = str1[0] + str1[-1]    # Первый и последний символы. Без пробелов.
    print('Первый и псоледний символы:', str2.replace(' ', ''))
    str4 = str1.upper()    # Верхний регистр.
    print('Верхний регистр:', str4)
    str5 = str1[::-1]    # Обратный порядок.
    print('Обратный порядок', str5)
    str6 = str1.isdigit()    # Проверка, что данные - числа.
    print('Строка состоит из цифр:', str6)

print('\nЗадание №5. Строка из двух слов. Поменять местами.')
str1 = "Hello world"
print(str1)
str2 = str1.replace('Hello', '.')    # Резерва места для замены
# print(str2)
str3 = str2.replace('world', 'Hello')    # Замена слова
# print(str3)
str4 = str3.replace('.', 'world')    # Заполнения резервного места
print(str4)
