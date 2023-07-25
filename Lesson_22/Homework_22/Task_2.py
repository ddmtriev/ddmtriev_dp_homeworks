print('Домашнее задание №22. Даукша Денис')
print('Задание №2. Создайте класс Робот создайте 2 типа оружия: меч, автомат '
      'Создайте 2 типа амуниции: броня, шлем'
      'Добавьте оружию и амуниции свои характеристики(например урон, прочность)'
      'Создайте своего робота с каким либо оружием(может быть несколько и брони может быть несколько.'
      'Так же может быть ничего)'
      'Выведите весь арсенал робота на экран')


class Rifle:

    def __init__(self, name, damage, strength):
        self.name = name
        self.damage = damage
        self.strength = strength

    def __str__(self):
        return f'{self.name} with damage:{self.damage} and strength:{self.strength}'


class Sword:

    def __init__(self, name, damage, strength):
        self.name = name
        self.damage = damage
        self.strength = strength

    def __str__(self):
        return f'{self.name} with damage:{self.damage} and strength:{self.strength}'


class Armor:

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __str__(self):
        return f'{self.name}, strength:{self.strength}'


class Helmet:

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __str__(self):
        return f'{self.name}, strength:{self.strength}'


class Robot:

    # armor = Armor('Jacket', 100)
    # helmet = Helmet('Moto-helmet', 200)
    # sword = Sword("Artur's", 500, 250)
    # rifle = Rifle('M16 Predator', 900, 1000)

    def __init__(self, name, armor_, helmet_, sword_, rifle_):
        self.name = name
        self.helmet = helmet_
        self.armor = armor_
        self.sword = sword_
        self.rifle = rifle_

    def __str__(self):
        return f'Robot {self.name}\n' \
               f'With armor: {self.armor}\n' \
               f'Helmet: {self.helmet}\n' \
               f'Sword: {self.sword}\n' \
               f'And rifle: {self.rifle}'


armor = Armor('Jacket', 100)
helmet = Helmet('Moto-helmet', 200)
sword = Sword("Artur's", 500, 250)
rifle = Rifle('M16 Predator', 900, 1000)
robo = Robot('Chappie', armor, helmet, sword, rifle)
print(robo)
