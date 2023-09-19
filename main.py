import turtle                 #allows you to use t unstead of turtle object 
from random import random     #imports random module

screen = turtle.Screen()      #creates a screen object
screen.setup(600, 400)        #setup screen size
screen.bgcolor("black")       # sets screen color



turtle1 = turtle.Turtle()     #creates turtles 
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
drawingTurtle = turtle.Turtle()

forward_valuex = 550
forward_valuey = 250
turn_value = 90

drawingTurtle.color("red")
drawingTurtle.penup()
drawingTurtle.goto(-275, 125)
drawingTurtle.pendown()
drawingTurtle.fillcolor("red")
drawingTurtle.begin_fill()
drawingTurtle.forward(forward_valuex)
drawingTurtle.right(turn_value)
drawingTurtle.forward(forward_valuey)
drawingTurtle.right(turn_value)
drawingTurtle.forward(forward_valuex)
drawingTurtle.right(turn_value)
drawingTurtle.forward(forward_valuey)
drawingTurtle.end_fill()




turtle1.penup()
turtle1.goto(0,100)




turtle.mainloop()