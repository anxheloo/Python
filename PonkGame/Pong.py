

import turtle

# interect with operating system through text commands
import os  # for apple and linux | to play sound
import winsound  # for windows  |  to play sound


# ------------------------------------------------------------------------ #
# BUILD THE WINDOW
# ------------------------------------------------------------------------ #

window = turtle.Screen()  # Create a window
window.title("Pong by @FreeCodeCAmp")  # Set the title
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Stops the window for updates, speeds the game


# ------------------------------------------------------------------------ #
# BUILD PADDLE A
# ------------------------------------------------------------------------

# turtle stands for model name,     Turtle stands for class name
paddle_a = turtle.Turtle()
# Sets the speed to maximum speed, if we dont use this, things are going to be slow
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# Consider this as x,y (boshti x dhe y)
paddle_a.goto(-350, 0)


# ------------------------------------------------------------------------ #
# BUILD PADDLE B
# ------------------------------------------------------------------------ #
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# 100 px tall and 20px wide
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# if we dont use this penup(), the paddle object will draw a line on the screen as it moves
paddle_b.penup()
paddle_b.goto(350, 0)


# ------------------------------------------------------------------------ #
# BUILD BALL
# ------------------------------------------------------------------------ #

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")  # Set the shape of the ball
ball.color("white")
ball.penup()
ball.goto(0, 0)        # X, Y cordinates for the ball to start
ball.dx = 0.1            # Every time ball moves to X,  it moves by 0.1 |   2 is very fast
ball.dy = 0.1            # Every time ball moves to Y, it moves by 0.1  |   2 is very fast


# ------------------------------------------------------------------------ #
# Pen
# ------------------------------------------------------------------------ #

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# if we dont use this penup(), the paddle object will draw a line on the screen as it moves
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
score_a = 0
score_b = 0
pen.write("Player A: " + str(score_a) + " Player B: " + str(score_b), align="center",
          font=("Courier", 24, "normal"))


# ------------------------------------------------------------------------ #
# BUILD FUNCTIONS TO MOVE THE paddleA, paddleB, Ball
# ------------------------------------------------------------------------ #

# Move paddleA Up
def paddle_a_up():
    y = paddle_a.ycor()  # Get the y cordinates
    y += 20  # Add 20 to the y cordinates
    paddle_a.sety(y)  # Set the new y


# Move paddleA Down
def paddle_a_down():
    y = paddle_a.ycor()  # Get the y cordinates
    y -= 20  # Add 20 to the y cordinates
    paddle_a.sety(y)  # Set the new y


# Move paddleB Up
def paddle_b_up():
    y = paddle_b.ycor()  # Get the y cordinates
    y += 20  # Add 20 to the y cordinates
    paddle_b.sety(y)  # Set the new y


# Move paddleB Down
def paddle_b_down():
    y = paddle_b.ycor()  # Get the y cordinates
    y -= 20  # Add 20 to the y cordinates
    paddle_b.sety(y)  # Set the new y


# ------------------------------------------------------------------------ #
    # LISTEN TO KEYBOARD BUTTONS
# ------------------------------------------------------------------------ #

# Keyboard binding
window.listen()  # Listen for keyboard input
# When the user press the "w" button, call the function paddle_a_up
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# ------------------------------------------------------------------------ #
# MAIN LOOP TO KEEP THE GAME GOING
# ------------------------------------------------------------------------ #

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking   |    What we want to happen when the ball hits the boarder
    # -------------------------------------------------------------------------------------------------------

    # The Ball Dimensions are 20px , the windown height is 600 px.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        file = "pongsound.wav"
        winsound.PlaySound(file, winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        file = "pongsound.wav"
        winsound.PlaySound(file, winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        # pen.write("Player A: " + str(score_a) + " Player B: " + str(score_b), align="center",
        #           font=("Courier", 24, "normal"))
        pen.clear()   # We clear the screen before updating cuz otherwise it will print above the existing
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",  # both are same, did it for the reason of .format
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # ----------------------------
    # Paddle and Ball Collisions
    # ----------------------------
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        file = "pongsound.wav"
        winsound.PlaySound(file, winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        file = "pongsound.wav"
        winsound.PlaySound(file, winsound.SND_ASYNC)
