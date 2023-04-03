# Imports turtle module
import turtle as t
t.showturtle()

# turns the background color to red
t.bgcolor("red")

t.penup()
t.setpos(10, 5)
t.pendown()

# Designing the letter S
t.pensize(15)
t.color("whitesmoke")
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Moving the pen next to the letter S
t.penup()
t.goto(40, -70)
t.pendown()

# turns the background color to firebrick
t.bgcolor("firebrick")

# Drawing the G
t.pensize(12)
t.color("slategray")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.right(90)
t.forward(15)
t.left(90 * 2)
t.forward(30)

# re position pen
t.penup()
t.goto(100, -50)
t.pendown()
t.left(100)

# turns the background color to maroon
t.bgcolor("maroon")

# Draw Star
t.pensize(6)
t.color("black")
t.forward(300)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300)

# re position pen
t.penup()
t.goto(80, -120)
t.pendown()
t.left(100)

# turns the background color to darkred
t.bgcolor("darkred")

# Draw Second Star
t.pensize(6)
t.color("black")
t.forward(300)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300 * 2)
t.right(144)
t.forward(300)

# re position pen
t.penup()
t.goto(-350, -100)
t.pendown()

# turns the background color to #bf0404
t.bgcolor("#bf0404")

# Draw's a circle around the stars
t.pensize(10)
t.speed(5)
t.color('black')
t.circle(-350)
t.end_fill()
t.done()