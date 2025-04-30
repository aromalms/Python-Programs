#draw a circle
import turtle
x=turtle.Turtle()
x.speed(4)
for i in range(5):
    x.fillcolor("red")
    x.begin_fill()
    x.circle(100,90)
    x.left(90)
    x.circle(100,90)
    x.left(20)
    x.end_fill()
turtle.done()