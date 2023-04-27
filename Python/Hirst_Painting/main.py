import turtle as t
import random
t.colormode(255)

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Hirst_Painting\hirst_image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75,
77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

arrow = t.Turtle()
arrow.speed("fastest")
arrow.hideturtle()

# arrow.begin_fill()
# ############
# arrow.dot(20, (202, 164, 110))
# arrow.penup()
# arrow.forward(50)
# arrow.dot(20, (147, 17, 19))
# arrow.forward(50)
# arrow.dot(20, "pink")
# ###########
# arrow.end_fill()

def hirst_painting():
    color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75,
77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

    for r in range(5):
        rand_col = color_list[random.randint(0,26)]
        arrow.penup()
        arrow.dot(20, rand_col)
        arrow.forward(50)

    arrow.backward(250)
    arrow.setheading(90)
    arrow.forward(30)
    arrow.dot(20, rand_col)
    arrow.setheading(0)
    
for i in range(5): 
    hirst_painting()

screen = t.Screen()
screen.exitonclick()

