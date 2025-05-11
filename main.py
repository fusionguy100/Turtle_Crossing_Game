import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

counter = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")
car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Player wins collision
    if player.ycor() > 280:
        scoreboard.level += 1
        scoreboard.scoreboard_update()
        player.reset_player()
        car_manager.speed_increase()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()