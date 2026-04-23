import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


screen = turtle.Screen()
screen.bgcolor("#87CEFF")
screen.title("The Sunflower")
screen.setup(800, 650)

def draw_sun():
    pen.penup()
    pen.goto(-375, 225)
    pen.pendown()
    pen.color("#FFCC33")
    pen.begin_fill()
    pen.circle(60)
    pen.end_fill()

def draw_vase():
    pen.penup()
    pen.goto(-50, -300)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    pen.forward(100)
    pen.left(60)
    pen.forward(75)
    pen.left(120)
    pen.forward(175)
    pen.left(120)
    pen.forward(75)
    pen.end_fill()

def draw_petal(color, pencolor):
    pen.color(color)
    pen.pencolor(pencolor)
    pen.begin_fill()
    pen.circle(100,60)
    pen.left(120)
    pen.circle(100,60)
    pen.left(120)
    pen.end_fill()

def draw_eye(x):
    pen.penup()
    pen.goto(x, 0)
    pen.begin_fill()
    pen.color("black")
    pen.pendown()
    pen.circle(5)
    pen.end_fill()

def draw_flower(petals):
    #Drawing the stem
    pen.penup()
    pen.home()
    pen.pensize(10)
    pen.goto(-5, 0)
    pen.color("lightgreen")
    pen.pendown()
    pen.begin_fill()
    pen.right(90)
    pen.forward(230)
    #drawing the petals
    pen.penup()
    pen.pensize(1)
    pen.goto(0, 0)
    pen.pendown()
    pen.begin_fill()
    for _ in range(petals):
        draw_petal("yellow", "orange")
        pen.left(360 / petals)
    pen.end_fill()
    #drawing the face of the flower
    pen.begin_fill()
    pen.color("orange")
    pen.goto(-35, 0)
    pen.circle(35)
    pen.end_fill()
    draw_eye(-17)
    draw_eye(17)

    
    
    

def draw_leaves():
    #drawing the leaves
    pen.penup()
    pen.home()
    pen.goto(-5, -200)
    pen.pensize(10)
    pen.pendown()
    for _ in range(2):
        draw_petal("lightgreen", "lawngreen")
        pen.left(90)
def draw_ground():
    #drawing ground
    pen.penup()
    pen.home()
    pen.goto(-400, -300)
    pen.color("#5C4033")
    pen.pendown()
    pen.begin_fill()
    pen.forward(800)
    pen.right(90)
    pen.forward(250)
    pen.right(90)
    pen.forward(800)
    pen.end_fill()

    
# Main Code
draw_sun()
draw_vase()
draw_flower(12) #put inside brackets how many petals do you want :)
draw_leaves()
draw_ground()

turtle.done()