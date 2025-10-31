#turtle square
import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(800,600)
square=turtle.Tuetle()
sides=4
lenght=90
angle=360.0/sides
for i in range(sides):
    square.forward(lenght)
    square.right(angle)
turtle.done()
