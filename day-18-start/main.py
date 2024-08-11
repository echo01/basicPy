# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle as t
import random
# import colorgram

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]


def draw_dash_line(distance, dash_size):
    for i in range(1, int(distance/(dash_size*2))):
        timmy.pendown()
        timmy.forward(dash_size)
        timmy.penup()
        timmy.forward(dash_size)


def draw_shape(d_size, n_angle):
    for n in range(n_angle):
        timmy.color(random.choice(colours))
        timmy.forward(d_size)
        timmy.left(360/n_angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r, g, b)
    return randomColor


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("midnight blue")
timmy.pensize(1)
timmy.speed("fastest")
t.colormode(255)

# for n in range(100):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))

draw_spirograph(1)


screen = t.Screen()
screen.exitonclick()



