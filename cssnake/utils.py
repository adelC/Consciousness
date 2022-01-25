import turtle
import time
import random

def init_turtle_env():
    # Snake head
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game for Consciousness")
    wn.bgcolor("grey")
    wn.setup(width=600, height=600)
    wn.tracer(0)  # Turns off the screen updates

    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)  