#rainbow benzene
import turtle
colors=["red","purple","blue","green","orange","yellow"]
t=turtle.Pen()
t.speed(0)
for x in range(50):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(59)
turtle.done()