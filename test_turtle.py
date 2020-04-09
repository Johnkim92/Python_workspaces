import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange" ]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(5)
length = 15

while length <100:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(10)
    length += 1

