from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.move_speed = 0.05
        
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.moving_distance_x = 7
        self.moving_distance_y = 7

    def move(self):
        new_x = self.xcor() + self.moving_distance_x
        new_y = self.ycor() + self.moving_distance_y
        self.goto(new_x, new_y)    

    def bounce(self):
        self.moving_distance_y *= -1
   
    def bounce_paddle(self):
        self.moving_distance_x *= -1
        self.move_speed *= 0.8

    def restart(self):
        self.goto(0, 0)
        self.moving_distance_x *= -1
    
        