#Package
import turtle
import winsound

#Screen setup
scr=turtle.Screen()
scr.title("Pong")
scr.bgcolor("blue")
scr.setup(width=800, height=600)
scr.tracer(0)

#Score
sa=0
sb=0

#A
a=turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.shapesize(stretch_wid=4, stretch_len=1)
a.penup()
a.goto(-350, 0)

#B
b=turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.shapesize(stretch_wid=4, stretch_len=1)
b.penup()
b.goto(350, 0)

#Ball
c=turtle.Turtle()
c.speed(0)
c.shape("circle")
c.color("white")
c.penup()
c.goto(0, 0)
c.dx=0.09
c.dy=-0.09

#Pen
p=turtle.Turtle()
p.speed(0)
p.color("white")
p.penup()
p.hideturtle()
p.goto(0,260)
p.write("Player A: 0   Player B: 0", align="center", font=("Courier", 22, "bold"))

#Functions
def a_up():
    y=a.ycor()
    y+=20
    a.sety(y)

def a_down():
    y=a.ycor()
    y-=20
    a.sety(y)

def b_up():
    y=b.ycor()
    y+=20
    b.sety(y)

def b_down():
    y=b.ycor()
    y-=20
    b.sety(y)

#Keyboard
scr.listen()
scr.onkeypress(a_up,"w")
scr.onkeypress(a_down,"s")
scr.onkeypress(b_up,"Up")
scr.onkeypress(b_down,"Down")

#Game loop
while True:
    scr.update()

    #Move
    c.setx(c.xcor()+c.dx)
    c.sety(c.ycor()+c.dy)
    #Border bounce
    if c.ycor()>290:
        c.sety(290)
        c.dy*=-1
        winsound.PlaySound("pong_sound.mp3", winsound.SND_ASYNC)

    if c.ycor()<-290:
        c.sety(-290)
        c.dy*=-1
        winsound.PlaySound("pong_sound.mp3", winsound.SND_ASYNC)


    if c.xcor()>390:
        c.goto(0,0)
        c.dx *=-1
        sa+=1
        p.clear()
        p.write("Player A: {}   Player B: {}".format(sa, sb), align="center", font=("Courier", 22, "bold"))
        winsound.PlaySound("pong_sound.mp3", winsound.SND_ASYNC)


    if c.xcor()<-390:
        c.goto(0,0)
        c.dx *=-1
        sb+=1
        p.clear()
        p.write("Player A: {}   Player B: {}".format(sa, sb), align="center", font=("Courier", 22, "bold"))
        winsound.PlaySound("pong_sound.mp3", winsound.SND_ASYNC)


    #Paddle the ball
    if (c.xcor() > 340 and c.xcor() < 350) and (c.ycor() < b.ycor()+40 and c.ycor() > b.ycor()-40):
        c.setx(340)
        c.dx*=-1
        winsound.PlaySound("pong_sound.mp3", winsound.SND_ASYNC)


    if (c.xcor() < -340 and c.xcor() > -350) and (c.ycor() < a.ycor()+40 and c.ycor() > a.ycor()-40):
        c.setx(340)
        c.dx*=-1
        winsound.PlaySound("pong_sound.mp3", winsound.SND_ASYNC)





