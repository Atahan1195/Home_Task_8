# class MyDescriptor:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __get__(self, instance, owner):
#         return self.n * instance.p
#
#     def __set__(self, instance, value):
#         self.n = value
#
#     def __delete__(self, instance):
#         ...
#
#
# class Box:
#     def __init__(self, x, y, z):
#         self.p = x * y * z
#
#     result = MyDescriptor(10)
#
#
# box_1 = Box(1, 2, 3)
# print(box_1.result)
# box_1.result = 100
# print(box_1.result)


# class MyDescriptor:
#
#     def __init__(self):
#         ...
#
#     def __get__(self, instance, owner):
#         p = 0.5 * (instance.a + instance.b + instance.c)
#         return (p * (p - instance.a) * (p - instance.b) * (p - instance.c)) ** 0.5
#
#     def __set__(self, instance, value):
#         self.n = value
#
#     def __delete__(self, instance):
#         ...
#
#
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
#     area = MyDescriptor()
#
#
# triangle_1 = Triangle(3, 4, 5)
# print(triangle_1.area)
# triangle_1.a = 3.5
# print(triangle_1.area)