#Подключение библиотек--------------------------------------------------------------------------------------------------

import turtle
import math
import random
import winsound

#-----------------------------------------------------------------------------------------------------------------------

#Настройка окна
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("8-bit SpaceWarS")

#-----------------------------------------------------------------------------------------------------------------------

#Регистрация форм
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("missile.gif")

#-----------------------------------------------------------------------------------------------------------------------

#Рамки игры
border = turtle.Turtle()
border.speed(0)
border.penup()
border.goto(-362.5,-300)
border.pensize(2.5)
border.pencolor("white")
border.pendown()
for i in range(2):
   border.fd(720)
   border.lt(90)
   border.fd(610)
   border.lt(90)
border.hideturtle()
border.penup()

#-----------------------------------------------------------------------------------------------------------------------

Score = 0

#-----------------------------------------------------------------------------------------------------------------------

#Классы фона 17 штук (прорисовка звезды)
class back(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(45, 124)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back1(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(67, 204)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back2(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(203, 124)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back3(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(102, 104)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back4(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(23, 54)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back5(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(54, 165)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back6(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(187, 254)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back7(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.goto(154, 243)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back8(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(87, 46)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back9(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(53, 87)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back10(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(54, 12)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back11(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(87, 43)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back12(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(76, 276)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back13(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(56, 23)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back14(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(241, 54)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back15(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(78, 254)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

class back16(turtle.Turtle):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(98, 154)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    draw_star(24, "yellow")

#-----------------------------------------------------------------------------------------------------------------------

#Класс персонажа


class player(turtle.Turtle):

    bulletstate = "Ready"
    playerspeed = 20

#Персонаж
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.speed(0)
        self.shape("player.gif")
        self.setheading(90)
        self.penup()
        self.goto(0, -250)

#-----------------------------------------------------------------------------------------------------------------------

#Движение вправо
    def move_right(self):
        x = player.xcor()
        x += player.playerspeed
        if x > 340:
            x = 340
        player.setx(x)

#-----------------------------------------------------------------------------------------------------------------------

# Движение влево
    def move_left(self):
        x = player.xcor()
        x -= player.playerspeed
        if x < -340:
            x = -340
        player.setx(x)

#-----------------------------------------------------------------------------------------------------------------------

# Выстрел
    def firebullet(self):
        if player.bulletstate == "Ready":
            player.bulletstate = "Fire"
            winsound.PlaySound('laser.wav', winsound.SND_ASYNC)

            x = player.xcor()
            y = player.ycor() + 20
            bullet.goto(x, y)
            bullet.showturtle()

#-----------------------------------------------------------------------------------------------------------------------

# Смерть игрока
    def death(self):
        self.hideturtle()

#-----------------------------------------------------------------------------------------------------------------------

enemyspeed = 2.3

#-----------------------------------------------------------------------------------------------------------------------

#Класс Врага
class enemy(turtle.Turtle):

    #Создание врага
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.speed(0)
        self.turtlesize(1.2, 1.2)
        self.shape("enemy.gif")
        self.penup()
        self.setheading(90)
        x = random.randint(-300, 300)
        y = random.randint(180, 260)  # 180.260
        self.goto(x, y)

    #-------------------------------------------------------------------------------------------------------------------

    # Физика попадания
    def collisionfire(self):
        bullet.hideturtle()
        winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)
        bullet.setposition(0, -400)

        x = random.randint(-300, 300)
        y = random.randint(180, 280)
        self.setposition(x, y)

    #-------------------------------------------------------------------------------------------------------------------

    # Скрыть
    def hide(self):
        self.hideturtle()

#-----------------------------------------------------------------------------------------------------------------------

player=player()

# ----------------------------------------------------------------------------------------------------------------------

# Спавн врага
enemies = []
for i in range(7):
    enemies.append(enemy())

# ----------------------------------------------------------------------------------------------------------------------

# Создание снаряда
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.speed(0)
bullet.shape("missile.gif")
bullet.turtlesize(0.5, 0.5)
bullet.penup()
bullet.hideturtle()
bullet.setheading(90)
bullet.goto(0, -240)

bulletspeed = 22

# ----------------------------------------------------------------------------------------------------------------------

#очки
scorepen = turtle.Turtle()
scorepen.pencolor("white")
scorepen.speed(0)
scorepen.up()
scorepen.setposition(-355, 280)
scorestring = "Score: %s" %Score
scorepen.write(scorestring, False, align= "left", font=("Arial", 14, "normal"))
scorepen.hideturtle()

# ----------------------------------------------------------------------------------------------------------------------

#cистема коллизии

def collisionplay(a, b):

    distance = math.sqrt(abs(math.pow((a.xcor()-b.xcor()), 2) + math.pow((a.ycor()-b.ycor()), 2)))
    if distance < 25:
        return True
    else:
        return False

def collision(a, b):

    distance = math.sqrt(abs(math.pow((a.xcor()-b.xcor()), 2) + math.pow((a.ycor()-b.ycor()), 2)))
    if distance < 20:
        return True
    else:
        return False

# ----------------------------------------------------------------------------------------------------------------------

#Бинды
turtle.listen()
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")
turtle.onkey(player.firebullet, "space")

# ------------------------------------------------------------------------------------------------------------------

#main loop

while True:
    for enemy in enemies:
        #enemy movement
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        # --------------------------------------------------------------------------------------------------------------

        #Move enemy back and down
        if enemy.xcor() > 325:

            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -325:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemyspeed *= -1
        # --------------------------------------------------------------------------------------------------------------

        #Система огня и очков
        if collisionplay(bullet, enemy):
            bullet.hideturtle()
            player.bulletstate = "Ready"
            enemy.collisionfire()

            Score += 10
            scorestring = "Score: %s" % Score
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if collision(player, enemy):

             for e in enemies:
                 e.hide
             player.death

             winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
             print("GAME OVER")
             break


        if enemy.ycor() < -200:
            for j in enemies:
                j.hide()
            player.death

            winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
            print("GAME OVER")
            break

        # --------------------------------------------------------------------------------------------------------------

    # движение снарядов
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 150:
        player.bulletstate = "Ready"

    if bullet.ycor() > 300:
        bullet.hideturtle()
        player.bulletstate = "Ready"

    # ------------------------------------------------------------------------------------------------------------------

delay = input()