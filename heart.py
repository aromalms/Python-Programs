import turtle
red=turtle.Turtle()
red.speed(0)
def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)
def heart():
    red.fillcolor("red")
    red.begin_fill()
    red.left(140)
    red.forward(112)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()
heart()
turtle.done()