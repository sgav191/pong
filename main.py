#!/usr/bin/env python3
import turtle
screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(1000,600)
screen.bgcolor("white")
#Left Paddle Code
leftpaddle = turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=6, stretch_len=2)
leftpaddle.penup()
leftpaddle.goto(-400,0)

#Right Paddle Code
rightpaddle = turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=6, stretch_len=2)
rightpaddle.penup()
rightpaddle.goto(400,0)
#Ball Code & Functions
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
bx = 5
by = -5
paddlesize = 50

# Displays the score



#Paddle Functions
paddlespeed = 20
def LeftPaddleUp():

	y = leftpaddle.ycor()
	y = y+paddlespeed
	if y < 250:
		leftpaddle.sety(y)
def LeftPaddleDown():
	y = leftpaddle.ycor()
	y = y-paddlespeed
	if y > -250:
		leftpaddle.sety(y)


def RightPaddleUp():
	y = rightpaddle.ycor()
	y = y+paddlespeed
	if y < 250:
		rightpaddle.sety(y)

def RightPaddleDown():
	y = rightpaddle.ycor()
	y = y-paddlespeed
	if y > -250:
		rightpaddle.sety(y)

#Keyboard Bindings
screen.listen()
screen.onkeypress(LeftPaddleUp,"e")
screen.onkeypress(LeftPaddleDown, "d")
screen.onkeypress(RightPaddleUp, "Up")
screen.onkeypress(RightPaddleDown, "Down")



while True:
	screen.update()
	newx = ball.xcor() + bx
	newy = ball.ycor() + by

	if newy < -280:
		by = by*-1

	if newy > 285:
		by = by*-1

	# COLLISON DETECTION
	# When testing for collison we need to allow for the ball width and height
	# So create 2 new variables which are the ball x + the ball width
	# and the ball y + the height
	# depending on the surface you are hitting you will need to adjust this setting

	# the paddle width is 35
	rpx = rightpaddle.xcor()-35
	lpx = leftpaddle.xcor()+35

	if newx > rpx:
		rptop = rightpaddle.ycor() - paddlesize
		rpbottom = rightpaddle.ycor() + paddlesize
		if newy > rptop and newy < rpbottom:
			bx = bx*-1

	if newx < lpx:
		lptop = leftpaddle.ycor() - paddlesize
		lpbottom = leftpaddle.ycor() + paddlesize
		if newy > lptop and newy < lpbottom:
			bx = bx*-1

	# Check if ball has hit the left hand side of the screen and
	# reset ball back to the center
	# change ball direction
	# increase the opponents score by 1 and display it

	# Check if ball has hit the right hand side of the screen and
	# reset ball back to the center
	# change ball direction
	# increase the opponents score by 1 and display it

	ball.setx(newx)
	ball.sety(newy)
