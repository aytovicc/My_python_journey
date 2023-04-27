from turtle import Turtle

ALIGMENT = "center"
FONT = ('Courier', 12, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):        
        super().__init__()
        
        self.score = 0
        
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def you_died(self):
        self.clear()
        self.color('yellow')
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"Ouch! You hit the wall. Your final score: {self.score}", align= ALIGMENT, font= ('Courier', 15, 'normal'))

    def you_ate_yourself(self):
        self.clear()
        self.color('yellow')
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"Ewww! You ate yourself. Your final score: {self.score}", align= ALIGMENT, font= ('Courier', 15, 'normal'))






