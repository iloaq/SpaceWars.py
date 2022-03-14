# Draw background and window borders

from internal.dependencies import *
from data import colors

# Description of the creation of stars in the background
class Star(turtle.Turtle):
    def __init__(self):
        super().__init__()
        x = random.randint(-330, 300)
        y = random.randint(-100, 300)
        angle = 144

        self.speed(15)
        self.fillcolor(colors.starColor)
        self.goto(x, y)
        self.begin_fill()
        for _ in range(5):
            self.forward(24)
            self.right(angle)
        self.end_fill()
        self.hideturtle()

# Scrren settings
screen = turtle.Screen()
screen.setup(720,610)
screen.bgcolor(colors.bgColor)
screen.title("Tarasyk,Kalyaskarov,Isenguzhin,Selimgerey")

# Border settings
border = turtle.Turtle()
border.speed(0)
border.penup()
border.goto(-362.5,-300)
border.pensize(3)
border.pencolor(colors.penColor)
border.pendown()
for i in range(2):
   border.fd(720)
   border.lt(90)
   border.fd(610)
   border.lt(90)
border.penup()
border.goto(-362.5,-200)
border.pendown()
border.fd(720)
border.hideturtle()
border.penup()



for i in range(10):
    Star()