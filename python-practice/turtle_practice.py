import turtle
# turtle.circle(50)


# skk = turtle.Turtle()
 
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
     
# turtle.done()

skk = turtle.Turtle()

skk.backward(80)
skk.right(90)
skk.forward(60)
skk.left(90)
skk.forward(30)
skk.backward(30)
skk.right(90)
skk.forward(50)
skk.left(90)
skk.forward(80)
skk.penup()
skk.forward(80)
skk.pendown()
for i in range(4):
    skk.forward(50)
    skk.right(90)

skk.clear()
nonte = turtle.Turtle()
fonte = turtle.Turtle()

nonte.shape("circle")
fonte.shape("square")

nonte.left(30)
nonte.forward(100)
fonte.backward(50)

monte= turtle.Turtle()
monte.setpos(-100,-100)
monte.forward(30)
monte.forward(30)
monte.shape("triangle")
fonte.clear()
fonte.shape("circle")
nonte.clear()
turtle.done()