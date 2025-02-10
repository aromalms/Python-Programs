#draw a circle
import turtle
x=turtle.Turtle()
x.speed(0)
for i in range(5):
    x.fillcolor("red")
    x.begin_fill()
    x.circle(190,90)
    x.left(90)
    x.circle(190,90)
    x.left(18)
    x.end_fill()
turtle.done()