from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        car_color = random.choice(COLORS)
        self.color(car_color)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y_coord = random.randint(-250, 250)
        self.x_coord = 300
        self.goto(self.x_coord, self.y_coord)


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_move = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Car()
            self.car_list.append(car)

    def move(self):
        remove_car = []
        for car in self.car_list:
            car.x_coord -= self.car_move
            car.goto(car.x_coord, car.y_coord)
            if car.x_coord == -320:
                remove_car.append(car)

        for car in remove_car:
            self.car_list.remove(car)

    def next_level(self):
        self.car_move += MOVE_INCREMENT

    def collision(self):
        self.car_move = 0
