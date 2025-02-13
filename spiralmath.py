#spiral using math
import turtle
import math
t=turtle.Turtle()
angle=0
for i in range(100):
    x=i*math.cos(math.radians(angle))
    y=i*math.sin(math.radians(angle))
    t.goto(x,y)
    angle+=10
turtle.done()