# def generator(n):
#     for i in range(n):
#         yield i
#
#
# # element = generator(5)
# # print(next(element))
# # print(next(element))
# # print(next(element))
#
# for i in generator(5):
#     print(i)

# def decorator(func):
#     def wrapper():
#         print('Start function')
#         func()
#         print('Stop function')
#
#     return wrapper
#
#
# @decorator
# def test_func1():
#     print('Test text 1')
#
# test_func1()
#
#
# def test_func2():
#     print('Test text 2')
#

# test_wrapped_1 = decorator(test_func1)
# test_wrapped_1

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(4))


# list1 = [1, 2, 3, 4, 5]
# for i in enumerate(list1):
#     print(i)
#
#
# for index, element in enumerate(list1):
#     print(index, element)
#     # print(element)

# print('Задание №1. Количество разрядов введенного целого числа.')
#
#
# def digits_of_number(n):
#     number_string = str(n)
#     digits = len(number_string)
#     print(f'В числе {n} {digits} разрядов.')
#
#
# number = int(input('Введите целое число. Ответ: '))
# digits_of_number(number)

# import math

# print('Задание №2. Площадь круга, прямоугольника или треугольника.')
#
# def circle_square(r):
#     return math.pi * r ** 2
#
# def tria_square(a):
#     return ((3 ** 1/2)/4) * a ** 2
#
# def rect_square(a, b):
#     return a * b
#
# figure = int(input('Выберите фигуру. (Круг - 1, треуголник - 2, прямоугольник 3). Ответ: '))
# if figure == 1:
#     radius = float(input('Введите радиус круга. Ответ: '))
#     print(f'Площадь круга: {circle_square(radius)}')
# elif figure == 1:
#     side = float(input('Введите сторону равносторонненого треугольника. Ответ: '))
#     print(f'Площадь равностороннего треугольника: {tria_square()}')
# else:
#     side_a = float(input('Введите сторону A прямоугольника. Ответ: '))
#     side_b = float(input('Введите сторону В прямоугольника. Ответ: '))
#     print(f'Площадь прямоугольника: {rect_square(side_a, side_b)}')

# import random
#
#
# print('Задание №3. Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне, \
# указанном пользователем с клавиатуры.')
#
#
# def rand_range(start, end):
#     lst = [random.randint(start, end) for i in range(10)]
#     print(lst)
#
#
# start = int(input('Введите начало диапазона. Ответ: '))
# end = int(input('Введите окончание диапазона. Ответ: '))
# rand_range(start, end)

# print('Задание №4.  Написать функцию, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.')
#
#
# def clocks(sec):
#     days = sec // 86400
#     hours = sec // 3600
#     mins = sec // 60
#     secs = sec % 60
#     print(f'{days}:{hours}:{mins}:{secs}')
#
#
# sec = int(input('Введите число секунд. Ответ: '))
# clocks(sec)


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