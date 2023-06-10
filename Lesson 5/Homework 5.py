import random

print('Домашнее задание №5. Даукша Денис.')

num = str(random.randint(1, 10))    # Чтобы сложить строки
color = random.randint(1, 2)
if color == 1:
    color = 'красное'
else:
    color = 'чёрное'
attempt = 1
comp_comb = str(num + ' ' + color)
# print(comp_comb)    Для проверки
print('\n')
while attempt <= 5:
    user_comb = input('Введите Вашу комбинацию. (Пр.: 3 красный )Ответ: ')
    user_comb = user_comb.lower()
    user_comb = user_comb.strip()
    attempt += 1
    if comp_comb == user_comb:
        print('Поздравляю! Вы выиграли! Жаль, что призов у нас нет, но лотерейку можете купить. Вдруг повезёт :)')
        exit()
    elif attempt > 5:
        print(f'\nЭто была последняя попытка. Повезёт в другой раз :( \nА вот загаданная комбинация: {comp_comb}')
    else:
        # attempt += 1
        print(f'Эх... Неудача. Попробуйте ещё раз. Попытка №{attempt}')
