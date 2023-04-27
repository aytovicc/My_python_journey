from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width= 960, height= 540)
# ! Gif dosyası Turtle_race folder'ı içinde ona ulaşmak için Turtle_race/ yapmayı unutma !
screen.bgpic('Turtle_race/beach_turtle.gif')


starting_positions = [0, 40, 80, -40, -80]
colors =["green", "black", "orange", "purple", "blue"]
turtles = []

for r in range(0, 5):
    turtles_number = int(r)
    turtle = Turtle(shape="turtle")
    turtle.color(colors[r])
    turtle.penup()
    turtle.goto(x= -460, y= starting_positions[r])
    turtles.append(turtle)

User_bet = screen.textinput("Turtle Race", "Which one of the turtle will win the race? Enter a color")

if User_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        
        if turtle.xcor() > 475:
            is_race_on = False
            if User_bet == colors[turtles_number]:
                print(f"You won the bet! {User_bet} has won the race.")
            else:
                print(f"You lost! You bet on {User_bet} but {colors[turtles_number]} won the race.")

        moving_distances = [5, 10, 15, 20]
        turtle.forward(random.choice(moving_distances))


screen.exitonclick()