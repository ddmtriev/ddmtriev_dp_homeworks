# print('#1')
# for i in range(1,20):
#     if i % 2 == 0:
#         print(i)
#
# print("\n#2")
# list1 = [1, 2, 5, 7, 'cat']
# print(list1)
#
# print('\n#3')
# a = int(input('Введите начало диапазона. Ответ: '))
# b = int(input('Введите окончание диапазона. Ответ: '))
# c = int(input('Введите шаг диапазона. Ответ: '))
# for i in range(a, b, c):
#     print(i)
#
# print('\n#4')
# list1 = ['cat', 'dog', 'flowers', 1, 2, 3]
# print(len(list1))

# print('\n#5')
# list1 = [1, 2, 5, 6, 7, 8]
# sum = 0
# mult = 1
# for i in list1:
#     sum += i
#     mult *= i
# print(sum)
# print(mult)

# print('\n#6')
# for i in range(54,9184):
#     if i % 5 == 0:
#         print(i)
#
# print('\n#7')
# list1 = [1, 2, 3, 5, 6, 7, 5, 6, 4, 5, 3, 3, 4, 5, 4, 5, 6, 5, 6, 5]
# num = int(input('Введите число, повторения которого будем искать. Ответ: '))
# print(f'Число {num} встречается в списке {list1.count(num)} раз')

# print('\n#8')
# list1 = [1, -2, -5, 3, 6, -8, 1, 4, 7]
# x1 = 0
# x2 = 0
# for i in list1:
#     if i > 0:
#         x1 += 1
#     else:
#         x2 += 1
# print(f'В списке {x1} положительных чисел.')
# print(f'В списке {x2} отрицательных чисел.')

# print('\n#9')
# a = int(input('Введите начало диапазона. Ответ: '))
# b = int(input('Введите окончание диапазона. Ответ: '))
# summa = 0
# kolichestvo = 0
# for i in range(a,b+1):
#     if i % 3 == 0:
#         kolichestvo += 1
#         summa += i
# print(summa/kolichestvo)

print('\n#10')
num1 = list(input('Введите семизначное число. Ответ: '))
for i in num1:
    if int(i) % 2 == 0:
        print(i)
