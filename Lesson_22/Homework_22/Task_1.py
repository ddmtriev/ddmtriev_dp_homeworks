import string

print('Домашнее задание №22. Даукша Денис')

print('Задание №1. Класс Alphabet'
      ' 1. Создайте класс Alphabet'
      ' 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: '
      '     1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.'
      ' 3. Создайте метод print(), который выведет в консоль буквы алфавита'
      ' 4. Создайте метод letters_num(), который вернет количество букв в алфавите'
      'Класс EngAlphabet'
      ' 1. Создайте класс EngAlphabet путем наследования от класса Alphabet'
      ' 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). '
      ' В качестве параметров ему будут передаваться обозначение языка(например, "En") и строка, состоящая из всех букв'
      ' алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).'
      ' 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.'
      ' 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится '
      ' ли эта буква к английскому алфавиту.'
      ' 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства '
      ' __letters_num.'
      ' 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.')


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return f'Letters of {self.lang} alphabet are: {self.letters}'

    def num_of_letters(self):
        return f'Number of letters in {self.lang} alphabet is: {len(self.letters)}'


alpha = Alphabet('En', string.ascii_uppercase)
print(alpha.print())
print(alpha.num_of_letters())


class EngAlphabet(Alphabet):

    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, x):
        if x in string.ascii_uppercase or x in string.ascii_lowercase:
            return f'True, {x} is in {self.lang} alphabet'
        else:
            return f'False, {x} is not in {self.lang} alphabet'

    def num_of_letters(self):
        return f'Number of letters in {self.lang} alphabet is: {EngAlphabet.__letters_num}'

    @staticmethod
    def example():
        return 'Text example: We hold these truths to be self-evident, that all men are created equal, ' \
               'that they are endowed by their Creator with certain unalienable Rights, ' \
               'that among these are Life, Liberty and the pursuit of Happiness.'


eng_alph = EngAlphabet()
check_letter = input('Enter the letter you want to check: ')
print(eng_alph.is_en_letter(check_letter))
print(eng_alph.num_of_letters())
print(EngAlphabet.example())
