# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import another_module
# print(another_module.another_variable)
# import turtle
# timmy = turtle.turtles()

from turtle import Turtle, Screen

# object = class
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkGreen", "DarkOrange")
# print(f"position : {timmy.position()}")
# timmy.forward(100)
# timmy.goto(50, 50)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# import PrettyTable
from prettytable import PrettyTable
# create object Table from PrettyTable Class
Table = PrettyTable()
Table.field_names = ["Pokemon Name", "Type"]

Table.add_row(["Pikachu", "Electric"])
Table.add_row(["Squirtle", "Water"])
Table.add_row(["Charmander", "Fire"])
Table.align = "l"

print(Table)


