print('Домашнее задание №13. Даукша Денис.')

print('\nЗаданеи №1. Простейший калькулятор.')

def plus(num1, num2):
    result = num1 + num2
    return result


def minus(num1, num2):
    result = num1 - num2
    return result


def mult(num1, num2):
    result = num1 * num2
    return result


def div(num1, num2):
    result = num1 / num2
    return result


num1 = int(input('Введите число 1. Ответ: '))
num2 = int(input('Введите число 2. Ответ: '))
operation = input('Введите желаемую операцию. (+, -, *, или /). Ответ: ')


if num1 == 0 and num2 == 0:
    print('Завершение программы')
else:
    if operation == '+':
        print(plus(num1, num2))
    elif operation == '-':
        print(minus(num1, num2))
    elif operation == '*':
        print(mult(num1, num2))
    else:
        try:
            div(num1, num2)
        except ZeroDivisionError:
            print('Деление на ноль. Повторите ввод.')
        else:
            print(div(num1, num2))

print('\nЗадание №2. Если в функцию передается кортеж, то посчитать длину всех его слов. Если список, \
то посчитать кол-во букв и чисел в нем. Число - количество нечетных цифр. Строка - количество букв.')


def calculate(input_data):
    if type(input_data) == tuple:
        total_len = sum([len(word) for word in input_data])
        return f'Длина всех слов кортежа: {total_len}'
    elif type(input_data) == list:
        counter_alpha = 0
        counter_num = 0
        input_data_str = ' '.join(map(str, input_data))
        print(input_data_str)
        for elem in input_data_str:
            if elem.isalpha():
                counter_alpha += 1
        for el in input_data:
            if type(el) == int:
                counter_num += 1
        return f'Кол-во букв в списке: {counter_alpha}. Кол-во чисел в списке: {counter_num}'
    elif type(input_data) == int:
        counter = 0
        input_data_str = str(input_data)
        for elem in input_data_str:
            if elem.isdigit() and int(elem) % 2 != 0:
                counter += 1
        return f'Количество нечётных цифр в числе {input_data}: {counter}'
    elif type(input_data) == str:
        counter_alpha = 0
        for elem in input_data:
            if elem.isalpha and elem != ' ':
                counter_alpha += 1
        return f'Количество букв в строке: {counter_alpha}'


print('Выберите тип вводимых данных: \n1: Строка \n2: Число \n3: Кортеж \n4: Список')
input_choice = int(input('Ваш выбор: '))
if input_choice == 1:
    input_data = input('Введите строку: ')
elif input_choice == 2:
    input_data = int(input('Введите число: '))
elif input_choice == 3:
    input_data = tuple(input('Введите кортеж: '))
else:
    input_data = list(input('Введите список: '))

print(calculate(input_data))
