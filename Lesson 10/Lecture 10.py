# # 1 способ
# file = open('Text.txt', 'r')
# print(*file)
# file.close()
#
# # 2 способ
# with open('Text.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines[3])
#
# # Запись
# with open('Text.txt', 'a') as file:
#     file.write('\nHello world')
#     print(file.read())
#
# with open(r'C:\Users\user\PycharmProjects\pythonLessons\data1.txt', 'r') as file:
#     print(file.read())
# import os
# os.replace(r'C:\Users\user\PycharmProjects\Lesson 6\new_text.txt', \
# r'C:\Users\user\PycharmProjects\Lesson 10\new_text.txt')

print('Лекция №10. Даукша Денис.')

# print('\nЗадание №1. В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел')
# with open('10.1.txt', 'w') as input_file:
#     input_file.write('1 a 2 b 3 c 4 d 5 e')    # Запись данных в файл
# with open('10.1.txt', 'r') as input_file:    # Чтение файла с использованием метода readlines
#     sum1 = 0
#     input_file = input_file.readlines()
#     input_file = ' '.join(input_file)    # Перевод строки внутри списка input_file в список елементов
#     for i in input_file:
#         if i.isdigit():    #
#             sum1 += int(i)
# print(sum1)

print('\nЗадание №2. Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию, \
а потом слова по возрастанию их длины.')
result_num_list = []
result_word_list = []
with open('10.2.txt', 'w') as input_file:
    input_list = [3, 'hello', 1, 'my', 4, 'dear', 2, 'friend', 5]
    for elem in input_list:
        input_file.write(f'{str(elem)}\n')
with open('10.2.txt', 'r') as input_file:
    r_input_list = input_file.readlines()
    for elem in r_input_list:
        elem = elem[:-1]
        if elem.isdigit():
            result_num_list.append(elem)
            result_num_list.sort()
        else:
            result_word_list.append(elem)
            word_len = len(elem)
            result_word_list.sort(key=len)
print(result_num_list)
print(result_word_list)
result_num_list.extend(result_word_list)
print(result_num_list)
