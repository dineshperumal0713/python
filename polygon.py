screen = turtle.Screen()

screen.bgcolor("green")
screen.setup(800, 600)

polygon = turtle.Turtle()


numsides = 4       
sidelength = 100   
angle = 360.0 / numsides  

for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
