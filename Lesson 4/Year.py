year = int(input('Введите год: '))    # Проверить високосный ли
if year % 400 == 0:
    print(f'{year} год является високосным.')
elif year % 4 == 0:
    if year % 100 != 0:
        print(f'{year} год является високосным.')
    else:
        print(f'{year} год НЕ является високосным.')
