# Simple pong in Python3
# Tutorial from Freecodecamp.org
#
# By Fran
# Acordate que es tu primer tutorial Fran, no tenés que entender aún todo lo que hacés
# solo tenés que emocionarte con el resultado para que tu monkey mind agarre impulso :)
#
# Part 2 Game Objects: Paddles and ball

import turtle

wn = turtle.Screen()
wn.title("Pong pong pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)      # Draw the paddle in the left side


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)      # Draw the paddle in the right side

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)      # Draw the ball in the middle



# Main Game Loop
while True:
    wn.update()
