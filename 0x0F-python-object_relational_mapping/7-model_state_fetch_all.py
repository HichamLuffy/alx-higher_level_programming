#!/usr/bin/python3
#venv\Scripts\activate
import turtle
from tkinter import PhotoImage

# Function to draw a heart
def draw_heart():
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# Function to write "I love you" inside the heart
def write_love_phrase():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.color("white")
    turtle.write("I love you", align="center", font=("Arial", 16, "normal"))

# Main function
def main():
    turtle.speed(2)
    turtle.bgcolor("black")
    turtle.color("red")
    draw_heart()
    write_love_phrase()

    # Get the canvas and save it to an image file
    canvas = turtle.getcanvas()
    canvas.postscript(file="heart_image.ps", colormode='color')

    turtle.hideturtle()
    turtle.done()

# Run the main function
if __name__ == "__main__":
    main()
