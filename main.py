import random
import turtle

from color_list import colors
from turtle import Turtle, Screen


def create_row(cursor):
    for _ in range(10):
        cursor.forward(50)
        color = random_color()
        cursor.dot(10, color)


def initialize_cursor():
    cursor = turtle.Turtle('circle', visible=False)
    cursor.penup()
    cursor.setpos(-300, -300)
    return cursor


def random_color():
    return random.choice(colors)


def update_cursor_position(cursor, x_pos, y_pos):
    cursor.setpos(x_pos, (y_pos + 50))


def run():
    """
    Runs the program to generate a picture similar to Damien Hirst.
    """
    cursor = initialize_cursor()
    for i in range(10):
        x_pos = cursor.pos()[0]
        y_pos = cursor.pos()[1]
        create_row(cursor)
        update_cursor_position(cursor, x_pos, y_pos)


screen = Screen()
screen.colormode(255)
run()
screen.exitonclick()
