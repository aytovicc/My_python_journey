from turtle import Turtle
ALIGMENT = "center"
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):

    def __init__(self, location):
        super().__init__()
        self.score = 0
        
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(location)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGMENT, font= FONT)     

    def score_up(self):
        self.score += 1
        self.clear()    