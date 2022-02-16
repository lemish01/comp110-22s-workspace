from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

colormode(255)

leo.begin_fill()
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0 
while (i<3):
    leo.forward(300)
    leo.left(120)
    i = i + 1