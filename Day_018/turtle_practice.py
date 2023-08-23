from turtle import Turtle, Screen
import random

screen = Screen()

tim = Turtle()
tim.shape("turtle")
tim.color("coral")


def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def draw_dash_line():
    for _ in range(20):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_shapes():
    screen.colormode(255)
    for sides in range(3, 11):
        tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        angle = 360 / sides
        for _ in range(sides):
            tim.forward(100)
            tim.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk():
    screen.colormode(255)
    tim.pensize(width=15)
    tim.speed(10)
    headings = [0, 90, 180, 270]
    for _ in range(150):
        tim.pencolor(random_color())
        tim.setheading(random.choice(headings))
        tim.forward(50)


def draw_spirograph():
    screen.colormode(255)
    tim.speed("fastest")
    shift = 10
    for _ in range(int(360 / shift)):
        tim.pencolor(random_color())
        tim.circle(radius=100)
        tim.setheading(tim.heading() + shift)


# draw_square()
# draw_dash_line()
# draw_shapes()
# random_walk()
draw_spirograph()

screen.exitonclick()
