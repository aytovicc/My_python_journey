import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor('black')
screen.title('Turtle Crossing Game')
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.go_up, "Up")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car 
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False


    # If turtle reaches other side
    if player.ycor() > 290:
        scoreboard.level_up()
        car_manager.level_up()
        player.go_to_start()
        screen.update()
          
screen.exitonclick()          