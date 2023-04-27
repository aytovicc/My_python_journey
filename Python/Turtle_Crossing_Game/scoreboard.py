from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()    

        self.level = 0

        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-270, 290)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:{self.level}", align= 'center', font= FONT)      

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()    

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align= 'center', font= FONT)    