# name_value = input('Введите Ваше имя: ')
# age_value = input('Введите Ваш возраст: ')
# city_value = input('Введите Ваш город: ')
# person = {'name': name_value, 'age': age_value, 'city': city_value}
# print(person['age'])

bmw_list = ['E53', 'E70', 'F15']
mercedes_list = ['W163', 'W164', 'W166']
dict_series = {'BMW X5': bmw_list, 'Mercedes ML': mercedes_list}
for series in dict_series:
    print(f'Первая модель в линейке: {series}: {dict_series[series][0]},\
    последняя модель в линейке: {series}: {dict_series[series][-1]}')
