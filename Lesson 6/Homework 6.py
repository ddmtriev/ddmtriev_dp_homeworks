print('Домашнее задание №6. Даукша Денис')

print('\nЗадание №1. Список. В словах посчитать гл/согл. Числа чёт/не чёт.')    # Если чётное, то посчитать \
# сумму цифр.Если нечётное, то заменить на 1 в списке. Слово - посчитать гл, согл.
list1 = [15, 48, 'hello', 6, 19, 'world']
print(f'Исходная строка: {list1}')
for num in list1:
    if isinstance(num, int):    # Проверяем, что элемент является числом
        if num % 2 == 0:    # Проверяем, что число четное
            digits_sum = sum([int(digit) for digit in str(num)])    # Считаем сумму цифр
            print(f'{num} - четное число, сумма цифр: {digits_sum}')
        else:
            list1[list1.index(num)] = 1   # Заменяем на 1
            print(f'{num} - нечетное число, заменено на 1')
vowels = ['a', 'e', 'i', 'o', 'u']
for word in list1:
    vowels_count = 0    # Чтобы для каждого элемента счётчик обнулялся
    consonants_count = 0
    if isinstance(word, str):    # Проверяем, что элемент является строкой
        word.lower()
        for letter in word:
            if letter.lower() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        print(f'Количество гласных: {vowels_count}, количество согласных: {consonants_count} в слове {word}')    \
            # Вывод только для строковых элементов списка
print(f'Новая строка: {list1}')

print('\nЗадание №2. Выполнить операции.')    # 1)Сложить два списка 2) Добавьте элемент 6 на 3 позицию.\
# 3)Удалите все текстовые переменные 4) Посчитайте количество элементов списка
list1 = [4, 6, 'pу', 'tell', 78]
list2 = [44, 'hello', 56, 'exept', 3]
list3 = list1 + list2
list4 = []
print(f'Объеденённый список: {list3}')
list3.insert(3, list3[6])
print(f'Список, в которм 6 элемент исходного добавлен на 3-ю позицию: {list3}')
for i in list3:
    if isinstance(i, int):
        list4.append(i)
print(f'Список, в котором исключены текстовые элементы: {list4}')
print(f'Количество элементов последней версии списка = {len(list4)}')

print('\nЗадание №3. Списки даны. Для каждого из списков найти второе наименьшее значение в нем')
list_of_lists = [[-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34]]
num_ = 0
for list_ in list_of_lists:
    list_.remove(min(list_))
    num_ += 1    # Не смог придумать, как бы отобразить исходные списки в выводе, \
    # а измененный список вызывает диссонанс с ответом(
    print(f'Второе минимальное значение в списке №{num_}: {min(list_)}')

print('\nЗадание №4. m и n. Порядок вывода в зависимости от того, какое больше.')    # В порядке возрастания, \
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

print('\nЗадание №5. 100 нулей. Первый и последний = 1')
list1 = [0 for i in range(100)]
list1[0] = 1
list1[-1] = 1
print(list1)
