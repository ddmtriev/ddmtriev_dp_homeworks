import csv
import pandas
import random

# data = [['Price', 'Volume', 'Result'],
#         ['12', '5', '60']]
#
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(data)

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#     for text in reader:
#         print(text)

# with open('data.csv', 'r') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     for text in reader:
#         print(text)

# data = pandas.read_csv('data.csv', delimiter=';')
# print(data)
#
# data1 = ['hello', 'world']
# with open('data1.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     for element in data1:
#         writer.writerow([element])

# with open('students_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(['Имя', 'Фамилия', 'Возраст'])
#     key = 1
#     while key == 1:
#         if key == 1:
#             name = input('Введите Имя: ')
#             if name == 'stop':
#                 key = 0
#                 print('Запись прервана пользователем.')
#                 exit()
#             surname = input('Введите Фамилию: ')
#             age = input('Введите Возраст: ')
#             data = [
#                 [name, surname, age]
#             ]
#             writer.writerows(data)
#         else:
#             data = [
#                 [name, surname, age]
#             ]
#             writer.writerows(data)
#             exit()

# list1 = ['ab_cd_e', 'abc', 'a_b_c', 'a__bc_d_', '__']
# print(f'Исходный список: {list1}')
# list2 = []
# for i in list1:
#     if '_' in i:
#         list2.append(i.replace('_', ' '))
# print(f'Новый список: {list2}')
#
# dict1 = {1: 10, 2: 20, 3: 30}
# print(f'Исходный словарь: {dict1}')
# res_list = []
# for i in dict1:
#     mult = i * dict1[i]
#     res_list.append(mult)
# print(f'Список произведений (Ключ * Значение): {res_list}')

# Обновляет список до тех пор, пока 30 есть в списке
# list1 = [random.randint(29, 35) for i in range(10)]
# print(list1)
# state = bool(30 in list1)
# print(state)
# while state is True:
#     if 30 in list1:
#         index = list1.index(30)
#         list1[index] = 250
#     else:
#         break
# print(list1)
#
# # ОБновляет список после первого вхождения
# list1 = [random.randint(29, 35) for i in range(10)]
# print(list1)
# if 30 in list1:
#     index = list1.index(30)
#     list1[index] = 250
# print(list1)

list1 = [random.randint(0, 10) for i in range(10)]
list2 = [1, 2, 3]
print(list1)
list1[0] = list2
print(list1)
list1[-1] = sum(list2)
print(list1)
