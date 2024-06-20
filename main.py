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
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_backward, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.reach_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.next_level()

    # Detect Player Collision with Car
    for car in car_manager.car_list:
        if player.distance(car) < 30 and player.ycor() in range(car.y_coord - 20, car.y_coord + 20):
            car_manager.collision()
            game_is_on = False
            break


scoreboard.game_over()

screen.exitonclick()
