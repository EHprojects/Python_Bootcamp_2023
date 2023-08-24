# import colorgram
#
# rgb_list = []
#
#
# def get_colors(num_colors):
#     # Extract 6 colors from an image.
#     colors = colorgram.extract('hirst.jpg', 12)
#     for color_obj in colors:
#         color_tup = (color_obj.rgb[0], color_obj.rgb[1], color_obj.rgb[2])
#         rgb_list.append(color_tup)
#
#
# get_colors(6)
# print(rgb_list)

from turtle import Turtle, Screen
import random

color_list = [(199, 13, 32), (250, 238, 18), (39, 76, 190), (38, 218, 71), (229, 159, 46), (237, 226, 5), (28, 39, 156),
              (215, 75, 13), (197, 15, 11)]

# 10 x 10 rows of spots
# dots size 20, 50 space

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
x_pos = -250
y_pos = -250

for row in range(10):
    for col in range(10):
        tim.goto(x_pos, y_pos)
        tim.color(random.choice(color_list))
        tim.dot(20)
        x_pos += 50
    x_pos = -250
    y_pos += 50


screen.exitonclick()
