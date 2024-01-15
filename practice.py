# class Cat:
#     __slots__ = ['name', 'age', 'color']
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f'Cat: {self.name}, {self.age}, {self.color}'
#
#
# class Cat:
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f'Cat: {self.name}, {self.age}, {self.color}'
#
#     def __getattr__(self, art_name):
#         print(art_name)
#         return 11
#
#
# cat_1 = Cat('Tom', 2, 'black')
# print(cat_1.type)
# print(cat_1.name)
# print(cat_1.voice)
#
#
# class Cat:
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f'Cat: {self.name}, {self.age}, {self.color}'
#
#     def __getattribute__(self, atr_name):
#         try:
#             return object.__getattribute__(self, atr_name)
#         except AttributeError:
#             if atr_name == 'voice':
#                 return 'Meow'
#             print(atr_name)
#             return 11
#
#
# cat_1 = Cat('Jack', 5, 'red')
# print(cat_1.type)
# print(cat_1.name)
# print(cat_1.voice)


# class Cat:
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f'Cat: {self.name}, {self.age}, {self.color}'
#
#     def __getattr__(self, item):
#         print(f'No such attribute: {item}')
#         return 11
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         print(f'Deleting: {item}')
#         del self.__dict__[item]
#
#
# cat_1 = Cat('Tom', 2, 'black')
# print(cat_1)
# cat_1.age = 5
# print(cat_1)
# cat_1.type = 'Home cat'
# print(cat_1.type)
# del cat_1.type
# print(cat_1.type)


# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f'Triangle: side_a = {self.a}, side_b = {self.b}, side_c = {self.c}'
#
#     def __getattr__(self, item):
#         if item == 'perimeter':
#             return self.a + self.b + self.c
#         elif item == 'area':
#             p = (self.a + self.b + self.c) / 2
#             return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#         else:
#             raise AttributeError
#
#
# triangle_1 = Triangle(3, 4, 5)
# print(triangle_1)
# print(triangle_1.perimeter)
# print(triangle_1.area)


# class Cat:
#     def __init__(self, __name, age,):
#         self.__name = __name
#         self.age = age
#
#     def get_name(self):
#         print('call get name')
#         return self.__name
#
#     def set_name(self, name):
#         print('call set name')
#         self.__name = name
#
#     def del_name(self):
#         print('call del name')
#         del self.__name
#
#     name = property(get_name, set_name, del_name)
#
#     def __str__(self):
#         return f'Cat: {self.__name}, {self.age}'
#
#
# cat_1 = Cat('Tom', 2)
# cat_1.name = 'Jack'
# print(cat_1.name)
# print(cat_1)


# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f'Triangle: side_a = {self.a}, side_b = {self.b}, side_c = {self.c}'
#
#     def get_area(self):
#         p = (self.a + self.b + self.c) / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#     def set_area(self, area):
#         raise AttributeError("You can't change area")
#
#     def del_area(self):
#         raise AttributeError("You can't delete area")
#
#     area = property(get_area, set_area, del_area)
#
#
# triangle_1 = Triangle(3, 4, 5)
# print(triangle_1)
# print(triangle_1.area)
# triangle_1.area = 100
# del triangle_1.area