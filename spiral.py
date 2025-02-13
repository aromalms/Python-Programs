#concentric circles
import turtle
x=turtle.Turtle()
x.speed(0)
for i in range(10):
    x.circle(20*i)
    x.right(90)
    x.penup()
    x.forward(20)
    x.pendown()
    x.left(90)
turtle.done()