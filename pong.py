# Pong Clone in Python 3
# Written by Patrick Lee

import turtle

wn = turtle.Screen()
wn.title("Pong Clone")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) 

# Main game loop
while True:
    wn.update()