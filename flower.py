import time
import turtle


def draw_petal(t, radius, angle,color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.end_fill()


screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(800, 600)
t = turtle.Turtle()
t.speed(0)
t.width(2)


num_petals = 8
initial_radius = 100
growth_factor = 1.3
angle = 360 / num_petals

colors=[["darkorange","darkred"],["purple","pink"],["darkred","darkorange"]]


for i in range(2, -1, -1):
    radius = initial_radius * (growth_factor ** i)
    for j in range(num_petals):
        draw_petal(t, radius, 60,colors[i][j%2])
        t.color("black",colors[i][j%2])
        time.sleep(0.2)
        t.right(angle)

t.penup()
t.goto(0, -20)
t.pendown()
t.color("black","purple")
t.begin_fill()
t.circle(20)
t.end_fill()

t.hideturtle()
screen.mainloop()

