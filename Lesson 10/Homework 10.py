import random    # Для 3

print('Домашнее задание №11. Даукша Денис.')

print('\nЗадание №1. Нужно записать в файл сначала слова в порядке возрастания их длины, \
а после цифры в порядке возрастания.')
result_num_list = []
result_word_list = []
with open('homework_10.1.txt', 'w') as input_file:
    input_list = [3, 'hello', 1, 'my', 4, 'dear', 2, 'friend', 5]
    for elem in input_list:
        if str(elem).isdigit():
            result_num_list.append(elem)
            result_num_list.sort()
        else:
            result_word_list.append(elem)
            result_word_list.sort(key=len)
    result_word_list.extend(result_num_list)
    input_file.write(f'{result_word_list}')

print('\nЗадание №2. Построчно записать данные, вводимые пользователем. Окончанте ввода пустая cтрока.')
with open('homework_10.2.txt', 'w') as input_file:
    input_string = input('\nВведите данные. Окончание ввода - пустая строка. Данные: ')
    input_file.write(f'{input_string}\n')
    while input_string != '':
        input_string = input('\nВведите данные. Окончание ввода - пустая строка. Данные: ')
        input_file.write(f'{input_string}\n')
    else:
        print('Завершение записи.')
        

print('\nЗадание №3. Посчитать количество строк в текстовом файле. Определить кол-во символов в каждой строке.')
with open('homework_10.3.txt', 'w') as input_file:
    input_list = [random.randint(0, 1000) for elem in range(random.randint(0, 100))]
    for elem in input_list:
        input_file.write(f'{str(elem)}\n')
with open('homework_10.3.txt', 'r') as input_file:
    read_list = input_file.readlines()
    print(read_list)
    for elem in read_list:
        num_of_strings = read_list.index(elem)
        len_of_string = len(elem[:-1])
        result_dict = {f'{num_of_strings}': len_of_string for elem in range(len(read_list))}
        print(f'Номер строки: {num_of_strings + 1}. Длина строки: {len_of_string}')
