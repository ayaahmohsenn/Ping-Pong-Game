#imported turtle module
import turtle
window = turtle.Screen() #initialize the screen
window.title("Ping Pong by Aya") #Title of the screen
window.bgcolor("black") #background color of the screen
window.setup(width=800, height=600) #a function that takes the width and the height of the screen
window.tracer(0) #prevent the window to update itself automatically

#Racket1
Racket1 = turtle.Turtle()  #initialize turtle object(shape)
Racket1.speed(0)  #set the speed of the animation - 0 Fastest
Racket1.shape("square") #set the shape of the object
Racket1.color("blue") #set the color of the shape
Racket1.shapesize(stretch_wid=5, stretch_len=1) #stretches the shape to meet the size
Racket1.penup() #stops the object from drawing lines
Racket1.goto(-350,0) #set the coordinates
#Racket2
Racket2 = turtle.Turtle()  #Creating Object
Racket2.speed(0)  #it means that the shape of the racket will be shaped in very high speed
Racket2.shape("square")
Racket2.color("red")
Racket2.shapesize(stretch_wid=5, stretch_len=1)
Racket2.penup()
Racket2.goto(350,0)
#Ball
ball = turtle.Turtle()  #Creating Object
ball.speed(0)  #it means that the shape of the racket will be shaped in very high speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0 , Player 2: 0", align = "center", font= ("Courier", 24, "normal"))

#functions//to move the rackets
def Racket1_up():
    y = Racket1.ycor() #get the y of racket 1
    y += 20 #set the y to be increased by 20
    Racket1.sety(y) #set the y of racket 1 to the new y coordinates

def Racket1_down():
    y = Racket1.ycor()
    y -= 20 #set the y to be decreased by 20
    Racket1.sety(y)

def Racket2_up():
    y = Racket2.ycor()
    y += 20
    Racket2.sety(y)

def Racket2_down():
    y = Racket2.ycor()
    y -= 20
    Racket2.sety(y)

#Keyboard bindings
window.listen() #tell the window to expect keyboard input
window.onkeypress(Racket1_up, "w") #when pressing "w", the func Racket1_up is being invoked
window.onkeypress(Racket1_down, "s")
window.onkeypress(Racket2_up, "r")
window.onkeypress(Racket2_down, "f")

#Main Game Loop
while True:
    window.update() #update the screen everytime the game runs
    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at zero, and everytime the loop runs, it increases 2.5 on the x-axis
    ball.sety(ball.ycor() + ball.dy) #ball starts at zero, and everytime the loop runs, it increases 2.5 on the y-axis

    #border check. top border +300px, and the bottom border -300px. ball is 20px
    if ball.ycor() > 290: #if ball is at top border
        ball.sety(290) #set y coordinates at +290px
        ball.dy *= -1 #reverse direction

    if ball.ycor() < -290: #if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #if ball is at the right border
        #ball.goto(0,0)
        ball.setx(390)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("Player 1: {} , Player 2: {}".format(score1, score2), align = "center", font= ("Courier", 24, "normal"))

    if ball.xcor() < -390: #if ball is at left border
        #ball.goto(0,0)
        ball.setx(-390)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} , Player 2: {}".format(score1, score2), align = "center", font= ("Courier", 24, "normal"))

    #Collision of racket and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Racket2.ycor() + 40 and ball.ycor() > Racket2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Racket1.ycor() + 40 and ball.ycor() > Racket1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1




