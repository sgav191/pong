#!/usr/bin/env python3
import turtle
screen = turtle.Screen()
screen.title("The Pong Identity")
screen.setup(1000,600)
turtle.bgcolor("white")
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
















#Paddle Functions
def LeftPaddleUp():
	
	y = leftpaddle.ycor()
	y = y+10
	if y < 250:
		leftpaddle.sety(y)
def LeftPaddleDown():
	y = leftpaddle.ycor()
	y = y-10
	if y > -250:
		leftpaddle.sety(y)
	

def RightPaddleUp():
	y = rightpaddle.ycor()
	y = y+10
	if y < 250:
		rightpaddle.sety(y)
		
def RightPaddleDown():
	y = rightpaddle.ycor()
	y = y-10
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
	rpx = rightpaddle.xcor()-10
	lpx = leftpaddle.xcor()
	if newx > rpx:
		rptop = rightpaddle.ycor() - paddlesize
		rpbottom = rightpaddle.ycor() + paddlesize
		if newy > rptop and newy < rpbottom:
			bx = bx*-1
	if newx < lpx:
		bx = bx*-1
		
	ball.setx(newx)
	ball.sety(newy)
	
