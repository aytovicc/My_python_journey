from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.color('olive')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def go_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)    