from turtle import Turtle, Screen

arrow = Turtle()
arrow.pencolor("darkgreen")
arrow.speed("fastest")

def move_forward():
    arrow.forward(10)

def move_backward():
    arrow.backward(10)

def anti_clockwise():
    arrow.left(20)

def clockwise():
    arrow.right(20)

def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()

screen = Screen()
screen.listen()

screen.onkey(key= "w",fun= move_forward)
screen.onkey(key= "s",fun= move_backward)
screen.onkey(key= "d",fun= clockwise)
screen.onkey(key= "a",fun= anti_clockwise)
screen.onkey(key= "c",fun= clear)


screen.exitonclick()








