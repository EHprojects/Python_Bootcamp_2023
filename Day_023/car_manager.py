from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_dist = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_dist)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True

    def increase_speed(self):
        self.move_dist += MOVE_INCREMENT
