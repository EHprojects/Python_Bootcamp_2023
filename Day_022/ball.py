from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dist = 10
        self.y_dist = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_dist
        new_y = self.ycor() + self.y_dist
        self.goto(new_x, new_y)

    def reverse_y(self):
        self.y_dist *= -1

    def reverse_x(self):
        self.x_dist *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.reverse_x()

