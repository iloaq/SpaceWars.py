# Collision calculation algorithm

from internal.dependencies import *

def collisionplay(a, b):

    distance = math.sqrt(abs(math.pow((a.xcor()-b.xcor()), 2) + math.pow((a.ycor()-b.ycor()), 2)))
    if distance < 25:
        return True
    else:
        return False