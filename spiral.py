#concentric circles
import turtle
import math
t=turtle.Turtle()
t.speed(0)
angle=0
for i in range(200):
    x=i*math.cos(math.radians(angle))
    y=i*math.sin(math.radians(angle))
    t.goto(x,y)
    angle+=10
turtle.done()