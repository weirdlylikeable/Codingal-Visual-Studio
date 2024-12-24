import turtle
screen = turtle.Screen()
pointer=turtle.Turtle()
screen.bgcolor("red")
pointer.width(5)

# triangle
pointer.forward(100)
pointer.left(120)
pointer.forward(100)
pointer.left(120)
pointer.forward(100)
pointer.left(30)

pointer.up()
pointer.forward(150)
pointer.left(90)
pointer.down()

# rectangle
pointer.forward(125)
pointer.right(90)
pointer.forward(75)
pointer.right(90)
pointer.forward(125)
pointer.right(90)
pointer.forward(75)
pointer.up()
pointer.left(90)
pointer.forward(150)
pointer.down()

# hexagon
pointer.forward(100)
pointer.right(60)
pointer.forward(100)
pointer.right(60)
pointer.forward(100)
pointer.right(60)
pointer.forward(100)
pointer.right(60)
pointer.forward(100)
pointer.right(60)
pointer.forward(100)
pointer.right(60)

screen.bgcolor("blue")

turtle.done()