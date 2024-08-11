# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle as t
import random

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
color_list = ["red", "green", "black", "brown", "blue"]
# color_list = ["red", "green", "black", "brown", "blue", "pink", "purple", "yellow", "violet"]
pos_start_list = [0, 25, 50, 75, 100, -25, -50, -75, -100]
list_of_turtle = []
winner_race = []
is_race_on = Falsep[]
screen = t.Screen()
screen.setup(width=500, height=500)
user_chose = screen.textinput(title="Make your bet.", prompt=f"Which turtle will win the race? Enter a color {color_list} :")

for n in range(5):
    tim = t.Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(color_list[n])
    tim.goto(-screen.window_width()/2+10, pos_start_list[n])
    list_of_turtle.append(tim)

if user_chose:
    is_race_on = True

while is_race_on:
    racer_pos_x = 0
    for racer in list_of_turtle:
        racer.forward(random.randint(1, 10))
        racer_pos_x = racer.position()
        if racer_pos_x[0] >= 230:
            is_race_on = False
            winner_race = racer
winner_color = list(winner_race.color())[0]
if winner_color == user_chose:
    user_chose = screen.textinput(title="Race result", prompt=f"The {winner_color} turtle is win a race. You Win.")
else:
    user_chose = screen.textinput(title="Race result", prompt=f"The {winner_color} turtle is win a race. You Lose.")
# bee = t.turtles()
#
# cee = t.turtles()
# dee = t.turtles()
# gee = t.Turtle()
# fee = t.Turtle()
# def move_forward():
#     tim.forward(10)
#
#
# def move_back_forward():
#     tim.backward(10)
#
#
# def turn_right():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def turn_left():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def return_home():
#     tim.penup()
#     tim.home()
#     tim.pendown()
#     screen.clearscreen()
#
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_back_forward, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=return_home, key="c")

screen.exitonclick()
