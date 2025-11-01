import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(800,600)
square = turtle.Turtle()
numsides = 4
sidelength = 90
for side in range(numsides):
    square.forward(sidelength)
    square.right(90)
turtle.done()