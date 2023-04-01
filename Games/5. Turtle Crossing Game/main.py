import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.player_move, "w")
screen.onkey(player.player_jump, "space")
screen.bgcolor("black")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # player reaches next level
    if player.is_at_finishline():
        player.reset_player()
        scoreboard.increase_score()
        car_manager.increase_level()

    # create and move cars
    car_manager.create_car()
    car_manager.car_move()

    # Detect collision with the cars
    for each_car in car_manager.all_cars:
        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()





