from internal.dependencies import *
from data import colors
from domain import collisions
from presentation import background

# Form registration
turtle.register_shape("assets/images/player.gif")
turtle.register_shape("assets/images/enemy.gif")
turtle.register_shape("assets/images/missile.gif")

# Description of creation and functions of the player's spaceship
class player(turtle.Turtle):

    bulletstate = "Ready"
    playerspeed = 20

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("assets/images/player.gif")
        self.setheading(90)
        self.penup()
        self.goto(0, -250)

    def move_right(self):
        x = player.xcor()
        x += player.playerspeed
        if x > 340:
            x = 340
        player.setx(x)

    def move_left(self):
        x = player.xcor()
        x -= player.playerspeed
        if x < -340:
            x = -340
        player.setx(x)

    def firebullet(self):
        if player.bulletstate == 'Ready':
            player.bulletstate = "Fire"
            winsound.PlaySound('assets/sounds/laser.wav', winsound.SND_ASYNC)

            x = player.xcor()
            y = player.ycor() + 20
            bullet.goto(x, y)
            bullet.showturtle()

    def death(self):
        self.hideturtle()

# Description of creation and functions of the enemy spaceship
class enemy(turtle.Turtle):
    enemyspeed = 5

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.turtlesize(1.2, 1.2)
        self.shape("assets/images/enemy.gif")
        self.penup()
        self.setheading(90)
        x = random.randint(-300, 300)
        y = random.randint(180, 260)  # 180.260
        self.goto(x, y)

    def collisionfire(self):
            bullet.hideturtle()
            winsound.PlaySound('assets/sounds/explosion.wav', winsound.SND_ASYNC)
            bullet.setposition(0, -400)

            x = random.randint(-300, 300)
            y = random.randint(180, 280)
            self.setposition(x, y)

    def hide(self):
        self.hideturtle()


player = player()

enemies = []
for i in range(7):
    enemies.append(enemy())

# Bullet settings
bulletspeed = 22

bullet = turtle.Turtle()
bullet.color(colors.bulletColor)
bullet.speed(0)
bullet.shape("assets/images/missile.gif")
bullet.turtlesize(0.5, 0.5)
bullet.penup()
bullet.setheading(90)
bullet.goto(-400,-400)
bullet.hideturtle()


# Score settings
Score = 0

scorepen = turtle.Turtle()
scorepen.pencolor(colors.penColor)
scorepen.speed(0)
scorepen.up()
scorepen.setposition(-355, 280)
scorestring = "Score: %s" %Score
scorepen.write(scorestring, False, align= "left", font=("Arial", 14, "normal"))
scorepen.hideturtle()

#Binds
turtle.listen()
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")
turtle.onkey(player.firebullet, "space")

#main loop
play = True

while play:
    for enemy in enemies:
        #enemy movement
        x = enemy.xcor()
        x += enemy.enemyspeed
        enemy.setx(x)

        #Move enemy back and down
        if enemy.xcor() > 325:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
                j.enemyspeed *= -1
        if enemy.xcor() < -325:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
                j.enemyspeed *= -1

        #Fire and score system
        if collisions.collisionplay(bullet, enemy):
            bullet.hideturtle()
            enemy.collisionfire()
            player.bulletstate = "Ready"

            Score += 10
            scorestring = "Score: %s" % Score
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if enemy.ycor() < -200:
            for j in enemies:
                j.hide()
            player.death()

            winsound.PlaySound('assets/sounds/gameover.wav', winsound.SND_ASYNC)
            print("GAME OVER")
            time.sleep(4)
            exit(0)

    # Bullet movement
    if player.bulletstate == 'Fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Bullet Status update
    if bullet.ycor() > 300:
        bullet.hideturtle()
        player.bulletstate = "Ready"