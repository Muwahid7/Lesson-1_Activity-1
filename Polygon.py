import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(400,500)
polygon=turtle.Turtle()
num_sides=6
side_length=90
angle=360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()