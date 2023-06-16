print('Домашнее задание №14. Даукша Денис.')

print('Задание №1. Николай знает, что кортежи являются неизменяемыми, но он с этим не готов соглашаться. \
Ученик решил создать функцию del_from_tuple(), которая будет удалять первое появление определенного элемента из кортежа\
по значению и возвращать кортеж без оного. Попробуйте повторить шедевр не признающего авторитеты начинающего \
программиста. К слову, Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией \
в исходном виде).')


def del_from_tuple(input_tuple):
    print('Исходный кортеж', input_tuple)
    del_elem = input('Введите элемент, который необходимо удалить. Ответ:')
    result_tuple = tuple([elem for elem in input_tuple if elem != del_elem])
    return f'Результат изменения кортежа: {result_tuple}'


input_tuple = tuple(input('\nВведите элементы кортежа через пробел. Ответ: ').split(' '))
print(del_from_tuple(input_tuple))

print('\nЗадание №2. Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество \
лайков (как в Facebook). Примеры: \
likes() -> "no one likes this" \
likes("Ann") -> "Ann likes this" \
likes("Ann", "Alex") -> "Ann and Alex like this" \
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this" \
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"')


def likes(l_list):
    if l_list == ['']:
        print('No one likes this')
    elif len(l_list) == 1:
        print(f'{l_list[0]} likes it')
    elif len(l_list) == 2:
        print(f'{l_list[0]} and {l_list[1]} like this')
    elif len(l_list) == 3:
        print(f'{l_list[0]}, {l_list[1]} and {l_list[2]} like this')
    elif len(l_list) > 3:
        print(f'{l_list[0]}, {l_list[1]} and {len(l_list[1:-1])} like this')


likes_list = input('\nВведите список тех, кому это понравилось(Через пробел): ').split(' ')
likes(likes_list)
