import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(800,600)
polygon=turtle.Turtle()
numsides=6
sidelenght=90
angle=360.0/numsides
for i in range(numsides):
    polygon.forward(sidelenght)
    polygon.right(angle)
turtle.done()

