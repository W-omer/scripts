import turtle



#paddle A
pdl_A =  turtle.Turtle()
pdl_A.speed(0)
pdl_A.shape("square")
pdl_A.color("white")
pdl_A.shapesize(stretch_wid=5, stretch_len=1)  
pdl_A.penup()
pdl_A.goto(-350, 0)

#paddle B
pdl_B =  turtle.Turtle()
pdl_B.speed(0)
pdl_B.shape("square")
pdl_B.color("white")
pdl_B.shapesize(stretch_wid=5, stretch_len=1)  
pdl_B.penup()
pdl_B.goto(350, 0)

#ball
Ball =  turtle.Turtle()
Ball.speed(1)
Ball.shape("square")
Ball.color("white") 
Ball.penup()
Ball.goto(0, 0)
Ball.dx = .2
Ball.dy = .2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Functions
def pdl_A_up():
    y = pdl_A.ycor()
    y += 20
    pdl_A.sety(y)

def pdl_A_down():
    y = pdl_A.ycor()
    y -= 20
    pdl_A.sety(y)

def pdl_B_up():
    y = pdl_B.ycor()
    y += 20
    pdl_B.sety(y)

def pdl_B_down():
    y = pdl_B.ycor()
    y -= 20
    pdl_B.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(pdl_A_up, "w")
wn.onkeypress(pdl_A_down, "s")
wn.onkeypress(pdl_B_up, "Up")
wn.onkeypress(pdl_B_down, "Down")

score_a = 0
score_b = 0

#main game loop
while True:
    wn.update()


    #move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle hits
    if Ball.xcor() > 340 and Ball.xcor() < 350 and (Ball.ycor() < pdl_B.ycor() + 50 and Ball.ycor() > pdl_B.ycor() - 50):
        Ball.setx(340)
        Ball.dx *= -1

    if Ball.xcor() < -340 and Ball.xcor() > -350 and (Ball.ycor() < pdl_A.ycor() + 50 and Ball.ycor() > pdl_A.ycor() - 50):
        Ball.setx(-340)
        Ball.dx *= -1

    

   





 
