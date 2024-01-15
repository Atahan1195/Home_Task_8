#                       Home Task - 8

# Task - 1 Создайте класс "Счет", обладающий приватным свойством "баланс".
# Используйте специальные методы для контроля доступа к этому свойству.
# Добавьте свойство balance с декоратором @property, которое возвращает значение баланса.
# Определите метод __setattr__, запрещающий непосредственное изменение значения баланса.
# Также определите метод __getattr__, возвращающий сообщение о том, что свойство не существует,
# если доступ к нему попытаться получить. Используйте этот класс для создания объекта счета
# и попробуйте изменить значение баланса и получить доступ к несуществующему свойству.


class Account:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return f'Свойство не существует'

    def set_balance(self, balance):
        raise AttributeError("You can't change balance")

    balance = property(get_balance, set_balance)


account_1 = Account(1000)
print(account_1.balance)


# Task - 2 Создайте класс "Пользователь", который имеет свойства first_name и last_name.
# Используйте декораторы @property для обеспечения доступа к этим свойствам.
# Определите метод __setattr__, запрещающий непосредственное изменение значений first_name и last_name.
# Используйте метод __getattr__, который возвращает сообщение о том, что свойство не существует,
# если попытаться получить доступ к несуществующему свойству. Создайте пользовательский объект
# и попробуйте изменить значение first_name и получить доступ к несуществующему свойству.


class User:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        return f'Свойство не существует'

    def set_first_name(self, first_name):
        raise AttributeError("You can't change first name")

    first_name = property(get_first_name, set_first_name)

    def get_last_name(self):
        return f'Свойство не существует'

    def set_last_name(self, last_name):
        raise AttributeError("You can't change last name")

    last_name = property(get_last_name, set_last_name)

    def __str__(self):
        return f'User: {self.__first_name}, {self.__last_name}'


user_1 = User('Ivan', 'Ivanov')
print(user_1.first_name)


# Task- 3 Создайте класс "Прямоугольник", имеющий приватные свойства width и height.
# Используйте декораторы @property для создания свойств width и height, возвращающих значение этих свойств.
# Определите метод __setattr__, запрещающий непосредственное изменение значений width и height.
# Используйте метод __getattr__, который возвращает сообщение о том, что свойство не существует,
# если попытаться получить доступ к несуществующему свойству. Добавьте метод area, вычисляющий площадь прямоугольника.
# Создайте объект прямоугольника и попытайтесь изменить значения width и height,
# а также получить доступ к несуществующему свойству и вычислить площадь прямоугольника.


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return f'Свойство не существует'

    def set_width(self, width):
        raise AttributeError("You can't change width")

    width = property(get_width, set_width)

    def get_height(self):
        return f'Свойство не существует'

    def set_height(self, height):
        raise AttributeError("You can't change height")

    height = property(get_height, set_height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'Rectangle area: {self.__width}, {self.__height}'


rectangle_1 = Rectangle(10, 20)
print(rectangle_1.area())
rectangle_1.width = 100
print(rectangle_1.width)
print(rectangle_1.height)






