import turtle

# Set up the turtle window and set the background color
turtle.setup(width=800, height=500)
turtle.bgcolor("#E0FFFF")

# Define the height and width of the flag
height = 300
width = 450

# Draw the green rectangle
turtle.penup()
turtle.goto(-225, -50)
turtle.pendown()
turtle.color("#138808")
#turtle.color("#FF9933")
turtle.begin_fill()
turtle.forward(width)
turtle.right(90)
turtle.forward(height/3)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height/3)
turtle.end_fill()

# Draw the white rectangle
turtle.penup()
turtle.goto(-225, -47)
turtle.pendown()
turtle.color("#FFFFFF")
turtle.begin_fill()
turtle.forward(width/3)
turtle.right(90)
turtle.forward(height*1.5)
turtle.right(90)
turtle.forward(width/3)
turtle.right(90)
turtle.forward(height*1.5)
turtle.end_fill()


# Draw the saffron rectangle
turtle.penup()
turtle.goto(225, 105)
turtle.pendown()
turtle.color("#FF9933")
#turtle.color("#138808")
turtle.begin_fill()
turtle.forward(width)
turtle.right(90)
turtle.forward(height/3)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height/3)
turtle.end_fill()

# Draw the circle in the center
turtle.penup()
turtle.goto(-65, 27)
turtle.pendown()
turtle.color("#000080")
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()

# Draw the 24 spokes of the wheel
turtle.penup()
turtle.goto(10, 25)
turtle.pendown()
turtle.color("#FFFFFF")
turtle.pensize(2)
for i in range(24):
    turtle.forward(75)
    turtle.backward(75)
    turtle.left(15)

# Hide the turtle and update the screen
turtle.hideturtle()
turtle.done()
