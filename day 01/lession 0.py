from turtle import *



speed(50)
width(5)
color("brown")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)        #door
begin_fill()
color("black")
left(90)

forward(90)
right(90)

forward(60)
right(90)

forward(90)
end_fill()

penup()             #roof
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60,120)
pendown()
color("blue")
begin_fill()
right(150)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
forward(80)
pendown()
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

exitonclick()