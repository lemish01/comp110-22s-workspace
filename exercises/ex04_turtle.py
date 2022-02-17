"""Turtle Scene Exercise."""

__author__ = "730407722"


from turtle import Turtle, colormode, done
import random 


def main() -> None:
    """The entrypoint of my scene."""
    turt: Turtle = Turtle()
    ts = turt.getscreen()
    colormode(255)
    ts.bgcolor(12, 54, 98)
    turt.speed(1000)
    stars_num: int = 0
    while stars_num < 50:
        x = random.randint(-500, 500)
        y = random.randint(100, 300)
        stars(turt, x, y)
        stars_num = stars_num + 1
    tree(turt, 50, 20, 50, 20, 100)
    forest_left(turt, 25, 25)
    forest_right(turt, 25, 25)
    done()


def tree_tri(dw: Turtle, x: float, y: float, z: float) -> None: 
    """Drawing a triangle at location x,y with z scale."""
    dw.penup()
    dw.goto(x, y)
    dw.pendown()  
    colormode(255)
    dw.color("forest green")
    dw.pencolor(79, 115, 81)
    dw.begin_fill()
    dw.fillcolor(42, 87, 54)
    i: int = 0 
    while (i < 3): 
        dw.left(240)
        dw.forward(z)
        dw.left(240)
        i = i + 1
    dw.end_fill()
    return 


def tree(dw: Turtle, x: float, y: float, z: float, width: float, length: float) -> None:
    """Drawing a tree by combining 3 triangles."""
    trunk(dw, x - 6, y - 144, width, length)
    tree_tri(dw, x, y - 65, 2.7 * z)
    tree_tri(dw, x, y - 30, 2 * z)
    tree_tri(dw, x, y, 1.5 * z)
    return


def trunk(dw: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Drawing the trunk of the tree at a location x,y withh length side and width side."""    
    dw.penup()
    dw.goto(x, y)
    dw.pendown()
    colormode(255)
    dw.color("brown")
    dw.pencolor(44, 35, 28)  
    dw.begin_fill()
    dw.fillcolor(44, 35, 28)
    i: int = 0 
    dw.seth(0)
    while i < 2: 
        dw.forward(width) 
        dw.right(90)
        dw.forward(length)
        dw.right(90)
        i = i + 1
    dw.end_fill()
    return


def forest_left(dw: Turtle, x: float, y: float) -> None: 
    """Drawing multiple trees to the left of the page."""
    tree_num: int = 0
    while tree_num < 5:
        x = x - 100
        tree(dw, x, 20, 50, 20, 100) 
        tree_num = tree_num + 1


def forest_right(dw: Turtle, x: float, y: float) -> None: 
    """Drawing multiple trees to the left of the page."""
    tree_num: int = 0
    while tree_num < 5:
        x = x + 100
        tree(dw, x, 20, 50, 20, 100)
        tree_num = tree_num + 1


def stars(dw: Turtle, x: float, y: float) -> None:
    """Draws a random array of stars in the sky."""
    dw.penup()
    dw.goto(x, y)
    dw.pendown()  
    colormode(255)
    dw.color("yellow")
    dw.pencolor(255, 250, 85)
    dw.begin_fill()
    dw.fillcolor(255, 250, 85)
    i: int = 0
    while i < 5:
        dw.forward(25)
        dw.right(145)
        i = i + 1
    dw.end_fill()
    return


if __name__ == "__main__":
    main()