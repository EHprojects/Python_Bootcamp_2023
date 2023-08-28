import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
loop_pass = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop_pass % 6 == 0:
        cars.create_car()

    cars.move_cars()

    if cars.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    if player.check_finish():
        scoreboard.update_score()
        player.reset_player()
        cars.increase_speed()

    loop_pass += 1

screen.exitonclick()
