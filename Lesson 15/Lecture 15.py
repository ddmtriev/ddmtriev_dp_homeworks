# print('Лекция №15. Даукша Денис.')
#
print('Задание №1.')
sm = lambda inch: inch * 2.54
inch_ = lambda sm_: sm_ / 2.54
km_ = lambda mi_: mi_ * 1.6
mi = lambda km: km / 1.6
pound = lambda kg: kg * 0.4536
kg_ = lambda pound_: pound_ / 0.4536
oz = lambda gram: gram * 28.3495
gram_ = lambda oz_: oz_ / 28.2495
us_gal = lambda lit: lit * 3.79
lit_ = lambda us_gal_: us_gal_ / 3.79
pint = lambda lit__: lit__ * 0.57
lit___ = lambda pint_: pint_ / 0.57

while True:
    inp_opper = int(input('Выберите вариант перевода: '
                          '\n1. Дюймы в сантиметры'
                         '\n2. Сантиметры в дюймы'
                         '\n3. Мили в километры'
                         '\n4. Километры в мили'
                         '\n5. Фунты в килограммы'
                         '\n6. Килограммы в фунты'
                         '\n7. Унции в граммы'
                         '\n8. Граммы в унции'
                         '\n9. Галлон в литры'
                         '\n10. Литры в галлоны'
                         '\n11. Пинты в литры'
                         '\n12. Литры в пинты'
                          '\nОтвет: '))
    if inp_opper == 0:
        break
    elif inp_opper == 1:
        inch = float(input('Введите значение в дюймах: '))
        if inch == 0:
            break
        print(f'Результат перевода {inch} дюймов в см: {sm(inch)}')
    elif inp_opper == 2:
        sm = float(input('Введите значение в см: '))
        if sm == 0:
            break
        print(f'Результат перевода {sm} см в дюймы: {inch_(sm)}')
    elif inp_opper == 3:
        mi = float(input('Введите значение в милях: '))
        if mi == 0:
            break
        print(f'Результат перевода {mi} миль в км {km_(mi)}')
    elif inp_opper == 4:
        km = float(input('Введите значение в км: '))
        if km == 0:
            break
        print(f'Результат перевода {km} км в мили: {mi(km)}')
    elif inp_opper == 5:
        pound = float(input('Введите значение в фунтах: '))
        if pound == 0:
            break
        print(f'Результат перевода {pound} фунтов в кг: {kg_(pound)}')
    elif inp_opper == 6:
        kg = float(input('Введите значение в кг: '))
        if kg == 0:
            break
        print(f'Результат перевода {kg} кг в фунты: {pound(kg)}')
    elif inp_opper == 7:
        oz = float(input('Введите значение в унциях: '))
        if oz == 0:
            break
        print(f'Результат перевода {oz} унций в г: {gram_(oz)}')
    elif inp_opper == 8:
        gram = float(input('Введите значение в г: '))
        if gram == 0:
            break
        print(f'Результат перевода {gram} г в унции: {oz(gram)}')
    elif inp_opper == 9:
        us_gal = float(input('Введите значение в галлонах: '))
        if us_gal == 0:
            break
        print(f'Результат перевода {us_gal} гал в л: {lit_(us_gal)}')
    elif inp_opper == 10:
        lit = float(input('Введите значение в л: '))
        if lit == 0:
            break
        print(f'Результат перевода {lit} л в галл: {us_gal(lit)}')
    elif inp_opper == 11:
        pint = float(input('Введите значение в пинтах: '))
        if pint == 0:
            break
        print(f'Результат перевода {pint} пинт в л: {lit___(pint)}')
    elif inp_opper == 12:
        lit = float(input('Введите значение в л: '))
        if lit == 0:
            break
        print(f'Результат перевода {lit} л в пинты: {pint(lit)}')
    else:
        print('Ввод неверный. Повторите ввод.')

print('Задание №2.')


def date(d, m, y):
    if d in range(1, 32) and m in range(1, 13) and y in range(1, 2025):
        return f'Дата: {day},{month},{year} - существует.'
    else:
        return'Такой даты не существует.'


day = int(input('Введите день.(число) Ответ: '))
month = int(input('Введите месяц.(число) Ответ: '))
year = int(input('Введите год.(число) Ответ: '))
print(date(day, month, year))

print('Задание №3.')


def find_next_square(input_num):
    int_div = int(input_num ** (1/2))
    if (input_num ** (1/2)) / int_div == 1:
        return f'{input_num} => {int(((input_num ** (1/2)) + 1) ** 2)}'
    else:
        return -1


inp_num = int(input('Введите целое число - идеальный квадрат. Ответ: '))
print(find_next_square(inp_num))
