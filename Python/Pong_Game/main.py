from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

paddle_right = Paddle((370, 0))
paddle_left = Paddle((-380, 0))
ball = Ball()
scoreboard_right = ScoreBoard((150, 270))
scoreboard_left = ScoreBoard((-150, 270))


screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard_left.update_scoreboard()
    scoreboard_right.update_scoreboard()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
  
    # Detect collision with paddles
    if ball.distance(paddle_right) < 49.9 and ball.xcor() > 350 or ball.distance(paddle_left) < 49.9 and ball.xcor() < -350:
        ball.bounce_paddle()
    
    # Detect if right paddle misses.   
    if ball.xcor() > 380:
        ball.restart()
        scoreboard_left.score_up()
        screen.update()
        scoreboard_left.update_scoreboard()
        time.sleep(1)

    # Detect if left paddle misses.
    if ball.xcor() < -380:
        ball.restart()
        scoreboard_right.score_up()
        screen.update()
        scoreboard_right.update_scoreboard()
        time.sleep(1)

screen.exitonclick()