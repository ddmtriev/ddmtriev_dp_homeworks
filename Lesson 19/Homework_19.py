print('Домашнее задание №19. Даукша Денис')
print('\nЗаданеи №1.'
      '1) Реализовать калькулятор с 4 методами: Сумма, вычитание , умножение, деление.'
      'Метод принимает 2 аргумента и возвращает результат. Невалидные данные должны быть обработаны.'
      'Валидатором является в программе метод, который будет проверять ваши аргументы на то, является ли они числом.')


class Calculator:

    def validate_number(self, num1, num2):
        is_val_n1 = isinstance(num1, int) or isinstance(num1, float)
        is_val_n2 = isinstance(num2, int) or isinstance(num2, float)
        if is_val_n1 and is_val_n2:
            print('Valid')
        else:
            raise Exception('Not valid')

    def plus(self, num1, num2):
        self.validate_number(num1, num2)
        return num1 + num2

    def minus(self, num1, num2):
        self.validate_number(num1, num2)
        return num1 - num2

    def mult(self, num1, num2):
        self.validate_number(num1, num2)
        return num1 * num2

    def div(self, num1, num2):
        self.validate_number(num1, num2)
        return num1 / num2


calc = Calculator()

while True:
    num_1 = int(input('Введите число №1. Ответ: '))
    num_2 = int(input('Введите число №2. Ответ: '))
    opper = input('Введите операцию. (+, -, /, *). Ответ: ')
    if opper == '+':
        print(calc.plus(num_1, num_2))
    elif opper == '-':
        print(calc.minus(num_1, num_2))
    elif opper == '/':
        try:
            print(calc.div(num_1, num_2))
        except ZeroDivisionError:
            print('Деление на ноль. Повторите ввод.')
    elif opper == '*':
        print(calc.mult(num_1, num_2))
    elif (num_1 == 0) and (num_2 == 0):
        print('Завершение программы.')
        break

print('\nЗадание №2. 2)	Функция sum(a,b) принимает 2 числа и возвращает их сумму. Написать декоратор, который '
      'возвращает ошибку если переданы не числовые параметры(например строка)')


def decorate(summa):
    def check(num_1, num_2):
        if (type(num_1) is int or type(num_1) is float) and (type(num_2) is int or type(num_2) is float):
            summa(num_1, num_2)
        else:
            print('Ошибка')
    return check


@decorate
def summ(num1, num2):
    print(num1 + num2)


num_1 = 1
num_2 = 4
summ(num_1, num_2)

print('Задание №3. Создайте класс Soda (для определения типа газированной воды),'
      'принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). '
      'В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» '
      'в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».')


class Soda:

    def show_my_drink(self, add=''):
        if add == '':
            return f'Обычная газировка'
        else:
            return f'Газировка с добавкой: {add}'


sd = Soda()
adding = input('Введите название добавки. Ответ: ')
print(sd.show_my_drink(adding))
