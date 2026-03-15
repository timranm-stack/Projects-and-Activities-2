import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Fun with Shapes")
screen.bgcolor("lightblue")  # change background color here

t = turtle.Turtle()
t.speed(3)

def draw_equilateral_triangle(side, color):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

def draw_rectangle(width, height, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_hexagon(side, color):
    t.color(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(side)
        t.left(60)
    t.end_fill()

# Move and draw triangle
t.penup()
t.goto(-200, 0)
t.pendown()
draw_equilateral_triangle(100, "yellow")

# Move and draw rectangle
t.penup()
t.goto(0, 0)
t.pendown()
draw_rectangle(150, 80, "green")

# Move and draw hexagon
t.penup()
t.goto(200, 0)
t.pendown()
draw_hexagon(60, "red")

t.hideturtle()
turtle.done()
