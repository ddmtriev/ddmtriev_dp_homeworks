# print('Задание №1. 2 целых, дробное и строка. ')    # Целые и дробное сложить. Строку вывести.
# num1 = int(input('Введите первое целое число. Ответ: '))
# num2 = int(input('Введите второе целое число. Ответ: '))
# string1 = input('Введите строку. Ответ: ')
# num3 = float(input('Введите дробное число. Ответ: '))
# result = num1 + num2 + num3
# print(f'Заданная строка: {string1}')
# print(f'Сумма заданных чисел: {result}')

# print('\nЗадание №2. 4 переменных. Int, float, bool, str.')   # Преобразовать числа в строки.
# num1 = int(input('Введите целое число. Ответ: '))
# num2 = float(input('Введите дробное число. Ответ: '))
# string1 = input('Введите строку. Ответ: ')
# bool1 = bool(input('Введите булевое значение. Ответ: '))
# num1_1 = str(num1)    # Преобразование целого числа в строку.
# num2_1 = str(num2)
# print(f'Целое число: {num1}')
# print(f'Дробное число: {num2}')
# print(f'Элемент под индексом 0 от целого числа: {num1_1[0]}')    # Проверка. У числа нельзя вызвать элемент под опр. индексом.
# print(f'Элемент под индексом 2 от дробного числа: {num2_1[2]}')
# print(f'Заданная строка: {string1}')
# print(f'Заданное булевое значение: {bool1}')

# print('\nЗадание №3. ФИО, возраст, город.')    # ФИО в одну строку. Возраст, город отдельно.
# surname = input('Введите Вашу фамилию. Ответ: ')
# name = input('Введите Ваше имя. Ответ: ')
# patronymic = input('Введите Ваше отчество. Ответ: ')
# age = int(input('Введите Ваш возраст. Ответ: '))
# city = input('Введите город Вашего проживания. Ответ: ')
# print(f'Ваше ФИО: {surname} {name} {patronymic}.')
# print(f'Ваш возраст: {age} лет.')
# print(f'Вы проживаете в городе {city}.')

print('\nЗадание №4. 3 числа и все мат.действия с ними')    # Действия нужно выполнять в переменных
num1 = int(input('Введите первое число. Ответ: '))
num2 = int(input('Введите второе число. Ответ: '))
num3 = int(input('Введите третье число. Ответ: '))
summ = num1 + num2 + num3
diff = num3 - num2 - num1
mult = num1 * num2 * num3
quo = num1 / num2 / num3
degree = num1 ** num2 ** num3
int_div = num1 // num2 // num3
rem_div = num1 % num2 % num3
print(f'Сумма зажанных чисел: {summ}')
print(f'Разность заданных чисел: {diff}')
print(f'Произведение заданных чисел: {mult}')
print(f'Частное заданных чисел: {quo}')
print(f'Результат возведения в степень: {degree}')
print(f'Результат целочисленного деления: {int_div}')
print(f'Остаток от деления: {rem_div}')

# Сложно понять ожидаемый результат, т.к. в условии не был обозначен порядок исп. чисел
