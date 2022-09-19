import turtle


def downmove():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def rightmove():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def upmove():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def leftmove():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)



turtle.shape('turtle')

turtle.onkey(downmove,'s')
turtle.listen()
turtle.onkey(rightmove,'d')
turtle.listen()
turtle.onkey(upmove,'w')
turtle.listen()
turtle.onkey(leftmove,'a')
turtle.listen()
turtle.onkey(turtle.reset,'Escape')
turtle.listen()

