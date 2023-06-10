# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     result = num1/num2
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# else:
#     print(f'Result^2 {result**2}')
# finally:
#     print('Program finished')

# try:
#     input_list = input('Enter number list(Divide by space): ')
#     input_list = input_list.split(' ')
#     result = 0
#     for i in input_list:
#         i = int(i)
#         result += i
#     finish_result = result/len(input_list)
# except ValueError:
#     print('The type of input data is incorrect.')
# else:
#     print(finish_result)
# finally:
#     print('The program has been finished.')

# try:
#     m_num = int(input('Введите число М(Кратность): '))
#     k_num = int(input('Введите число К(Определяющая диапазона): '))
#     for i in range(k_num, k_num + 100):
#         if i % m_num == 0 and i > k_num:
#             print(i)
# except ValueError:
#     print('Тип вводимых данных неверен. Повторите ввод.')
# else:
#     print(i)
# finally:
#     print('Завершение программы.')

# try:
#     min_num = int(input('Введите минимальное число: '))
#     max_num = int(input('Введите максимальное число: '))
#     sum = 0
#     for i in range(min_num + 1, max_num):
#         if i > min_num and i < max_num:
#             sum += i
# except ValueError:
#     print('Тип вводимых данных неверен. Повторите ввод.')
# else:
#     print(sum)
# finally:
#     print('Завершение программы.')
#
# try:
#     a_hours = int(input('Введите минимальное количество часов сна: '))
#     b_hours = int(input('Введите максимальное количество часов сна: '))
#     h_hours = int(input('Введите Ваше актуальное количество часов сна: '))
#     if (h_hours >= a_hours) and (h_hours <= b_hours):
#         print('Это нормальное количество часов сна.')
#     elif h_hours < a_hours:
#         print('Беда. Это недосып!')
#     else:
#         print('Карамба! Это пересып. Проснись и пой!!!')
# except ValueError:
#     print('Ошибка. Повторите ввод.')
# finally:
#     print('Завершение программы.')

# try:
#     input_num = int(input('Введите число n: '))
#     if input_num in range(0, 10):
#         result = input_num + int(str(input_num)*2) + int(str(input_num)*3)
# except ValueError:
#     print('Ошибка. Повторите ввод.')
# else:
#     print(result)
# finally:
#     print('Завершение программы.')

try:
    input_num = int(input('Введите число ключей словаря: '))
    keys_list = [i for i in range(input_num)]
    dict1 = {key: {'name': input('Введите имя: '), 'email': input('Введите email: ')} for key in keys_list}
except ValueError:
    print('Данные введены неверно.')
else:
    print(dict1)
finally:
    print('Завершение программы.')
