#draw a right triangle
import turtle
import math
x=turtle.Turtle()
x.forward(90)
x.left(90)
x.forward(90)
x.left(135)
y=math.sqrt(90**2+90**2)
x.forward(y)
turtle.done()