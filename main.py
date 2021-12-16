# # # # # class ClassName:
# # # # #     # Class Attributes
# # # # #     # __init__()
# # # # #     # Methods
# # # #
# # # # # SELF MEANS INSTANCE THAT IS CURRENTLY BEING CREATED
# # # # class House:
# # # #
# # # #     def __init__(self, price):
# # # #         self.price = price
# # # #
# # # # # class Backpack:
# # # # #
# # # # #     def __init__(self, color, size):
# # # # #         self.item = []
# # # # #         self.color = color
# # # # #         self.size = size
# # # #
# # # # # HOW TO DEFINE INSTANCE ATTRIBUTES IN A CIRCLE, RECTANGLE, AND MOVIE CLASS
# # # # class Circle:
# # # #
# # # #     def __init__(self, radius):
# # # #         self.radius = radius
# # # #         self.color = "Blue"
# # # #
# # # # class Rectangle:
# # # #
# # # #     def __init__(self, length, width):
# # # #         self.length = length
# # # #         self.width = width
# # # #
# # # # class Movie:
# # # #
# # # #     def __init__(self, title, year, language, rating):
# # # #         self.title = title
# # # #         self.year = year
# # # #         self.language = language
# # # #         self.rating = rating
# # #
# # # # HOW TO CREATE INSTANCES
# # # # class Backpack:
# # # #
# # # #     def __init__(self, no_book):
# # # #         self.item = []
# # # #         self.no_book = no_book
# # # # my_backpack = Backpack(9)
# # # # print(my_backpack)
# # #
# # # # class Rectangle:
# # # #
# # # #     def __init__(self, length, width):
# # # #         self.length = length
# # # #         self.width = width
# # #
# # # # CODING EXERCISE
# # # # class Dog:
# # # #
# # # #     def __init__(self):
# # # #
# # # #
# # # # my_rectangle = Rectangle(5, 7)
# # # # print(my_rectangle)
# # #
# # # # HOW TO ACCESS INSTANCE ATTRIBUTES
# # # class Backpack:
# # #
# # #     def __init__(self, color, size):
# # #         self.items = []
# # #         self.color = color
# # #         self.size = size
# # #
# # #
# # # my_backpack = Backpack("red", 'M')
# # # your_backpack = Backpack("blue", 'S')
# # #
# # # print("My backpack: ")
# # # print(my_backpack.color)
# # # print(my_backpack.size)
# # #
# # # print("Your backpack: ")
# # # print(your_backpack.color)
# # # print(your_backpack.size)
# # #
# # # DEFAULT VALUE ASSIGNMENT
# # class Circle:
# #
# #     # def __init__(self, radius=5, color):#wrong
# #     def __init__(self, color, radius=5):#correct
# #         self.radius = radius
# #
# # my_circle = Circle(8, "Blue")
# # print(my_circle.radius)
# # # print(my_circle.color)
# # #
#
# class Circle:
#
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
# my_circle = Circle(6, "red")
#
# print(my_circle.radius)
# print(my_circle.color)
#
# my_circle.radius = 15
# my_circle.color = "Yellow"
#
# print(my_circle.radius)
# print(my_circle.color)
