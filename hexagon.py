import turtle
hex=turtle.Turtle()
turtle.bgcolor("blue")
hex.fillcolor("yellow")
hex.begin_fill()
for i in range(6):
    hex.forward(100)
    hex.right(60)
hex.end_fill()
turtle.done()