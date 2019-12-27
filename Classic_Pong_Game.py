import turtle

# Game window/screen setup
screen = turtle.Screen()
screen.title("Pong by Shehzad")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=1400, height=800)    

# danda_a
danda_a = turtle.Turtle()
danda_a.penup()
danda_a.speed(0) # animation speed
danda_a.shape("square")
danda_a.color("white")
danda_a.goto(-650,0)
danda_a.shapesize(stretch_wid=4, stretch_len=1)

# danda_b
danda_b = turtle.Turtle()
danda_b.penup()
danda_b.speed(0) # animation speed
danda_b.shape("square")
danda_b.color("white")
danda_b.goto(650,0)
danda_b.shapesize(stretch_wid=4, stretch_len=1)

# gaind/ball
gaind = turtle.Turtle()
gaind.penup()
gaind.speed(0) # animation speed
gaind.shape("circle")
gaind.color("white")
gaind.goto(0,0)
gaind.dx = 0.5
gaind.dy = 0.5

# Scoring Pen
pen = turtle.Turtle()
pen.speed(0)
pen.up()
pen.color('white')
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align= 'center',font=('Courier',15,'normal'))
score_a = 0
score_b = 0

# Functions
def danda_a_up():
    y = danda_a.ycor()
    y += 25
    danda_a.sety(y)

def danda_a_down():
    y = danda_a.ycor()
    y -= 25
    danda_a.sety(y)
    
def danda_b_up():
    y = danda_b.ycor()
    y += 25
    danda_b.sety(y)

def danda_b_down():
    y = danda_b.ycor()
    y -= 25
    danda_b.sety(y)
    
# Keyboard Binding
screen.listen()
screen.onkeypress(danda_a_up, 'w')
screen.onkeypress(danda_a_down, 's')
screen.onkeypress(danda_b_up, 'Up')
screen.onkeypress(danda_b_down, 'Down')


# Main game loop
while True:
    
    screen.update()
    
    # ball/gaind moving 
    gaind.sety(gaind.ycor() + gaind.dy)
    gaind.setx(gaind.xcor() + gaind.dx)
    
    # Setting Game borders
    # Top Border
    if gaind.ycor() >= 400:
        gaind.dy *= - 1
        
    # Bottom Border
    if gaind.ycor() <= -400:
        gaind.dy *= -1
        
    # Right Border and Scoring
    if gaind.xcor() >= 700:
        gaind.goto(0,0)
        gaind.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align= 'center',font=('Courier',15,'normal'))
    
    # Left Border and Scoring
    if gaind.xcor() <= -700:
        gaind.goto(0,0)
        gaind.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align= 'center',font=('Courier',15,'normal'))
        
    # Ball/Gaind collision with danday
    
    if (gaind.xcor() > 640 and gaind.xcor() < 655) and gaind.ycor() < danda_b.ycor() + 50 and gaind.ycor() > danda_b.ycor() - 50:
        gaind.dx *= -1 
    
    if (gaind.xcor() < -640 and gaind.xcor() > -655) and gaind.ycor() < danda_a.ycor() + 50 and gaind.ycor() > danda_a.ycor() - 50:
        gaind.dx *= -1 