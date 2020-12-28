import turtle
box = turtle.Screen()
box.bgcolor("yellow")
toy = turtle.Turtle()
toy.color("red")
toy.shape("turtle")
dist = 2
for i in range(100):
    toy.forward(dist)
    toy.left(45)
    toy.forward(dist)
    dist += 2
box.exitonclick()
