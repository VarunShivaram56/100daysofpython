from turtle import Turtle, Screen
import random

timmy= Turtle()
timmy.shape("turtle")
#timmy.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 10):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)

"""for _ in range(3):
    timmy.forward(100)
    timmy.right(120)

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

for _ in range(5):
    timmy.forward(100)
    timmy.right(72)

for _ in range(6):
    timmy.forward(100)
    timmy.right(60)

for _ in range(7):
    timmy.forward(100)
    timmy.right(51.42857142857143)  # 360/7

for _ in range(8):
    timmy.forward(100)
    timmy.right(45)
"""


















screen=Screen()
screen.exitonclick()