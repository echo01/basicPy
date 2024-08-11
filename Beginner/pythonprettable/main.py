# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask

from prettytable import PrettyTable
# create object Table from PrettyTable Class
Table = PrettyTable()
Table.field_names = ["Pokemon Name", "Type"]

Table.add_row(["Pikachu", "Electric"])
Table.add_row(["Squirtle", "Water"])
Table.add_row(["Charmander", "Fire"])
Table.align = "l"

print(Table)
