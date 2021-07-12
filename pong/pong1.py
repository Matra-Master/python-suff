# Simple pong in Python3
# Tutorial from Freecodecamp.org
#
# By Fran
# Acordate que es tu primer tutorial Fran, no tenés que entender aún todo lo que hacés
# solo tenés que emocionarte con el resultado para que tu monkey mind agarre impulso :)
#
# Part 1 Starting with a simple 800x600 window

import turtle

wn = turtle.Screen()
wn.title("Pong pong pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Main Game Loop
while True:
    wn.update()