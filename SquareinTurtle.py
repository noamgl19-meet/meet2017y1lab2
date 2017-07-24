import turtle
#inserting variubles
side_length = 50

turtle.penup()​ ​ #Pick up the pen so it doesn’t draw
turtle.goto(0,0)​ ​ #Move the turtle to the
#position, -200, -100, on
#the screen
turtle.pendown()​ ​ #Put the pen down to start
#drawing
#Draw the square:
turtle.goto(0,side_length)
turtle.goto(side_length,side_length)
turtle.goto(side_length,0)
turtle.goto(0,0)
# ...and end it before the next line.
turtle.mainloop()
