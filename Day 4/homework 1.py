#we really want to paint a house well me I can't wait until I will start it is going to be fantastic
from turtle import*
#we want to paint a house
#step 1: draw a square 
speed(30)
width(7)

color("blue")
forward(200)
left(90)
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square
forward(70)
left(90)
color("red")
forward(120)
right(90)
forward(60)
right(90)
forward(120)

color("gold")
penup()
goto(200 , 200)
pendown()
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(50 , 100)
color("orange")
pendown()
left(30)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)

#end of window N.1

penup()
goto(150,100)
color("orange")
pendown()
right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)

#end of window N.2

penup()
goto(120 , 190)
color("orange")
pendown()
left(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)


#house 2

penup()
goto(-5 , 0)
color("blue")
pendown()
backward(200)
right(90)
backward (200)
right(90)
backward(200)
right(90)
backward(200)
right(90)
#door 2
backward(70)
right(90)
color("red")
backward(120)
left(90)
backward(60)
left(90)
backward(120)

#window 2   N.1
penup()
goto(-15 , 60)
color("yellow")
pendown()
right(0)
forward(60)
right(90)
backward(40)
right(90)
forward(60)
right(90)
backward(40)

#House 2    window N.2
penup()
goto(-75 , 190)
pendown()
left(0)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)


penup()
goto(-199,75)
color("orange")
pendown()
right(90)
forward(55)
left(90)
forward(35)
left(90)
forward(55)
left(90)
forward(35)



color("gold")
penup()
goto(0 , 200)
pendown()
right(150)
forward(205)
left(120)
forward(200)


#House N.3   

penup()
goto(-203 , 0)
color("blue")
pendown()
right(150)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#House N.3 door

penup()
goto(-270 , 0)
pendown()
color("Purple")
left(90)
forward(120)
left(90)
forward(60)
left(90)
forward(120)

#House N.3 window 1

penup()
goto(-215 , 60)
pendown()
color("Gold")
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)

#House N.3 window 2

penup()
goto(-280 , 185)
pendown()
forward(53)
right(90)
forward(40)
right(90)
forward(53)
right(90)
forward(40)

#House N.3 window 3

penup()
goto(-343 , 60)
pendown()
backward(40)
right(270)
forward(53)
right(90)
forward(40)
right(90)
forward(53)


penup()
goto(-205 , 200)
pendown()
color("gold")
right(150)
forward(205)
left(120)
forward(200)


#Moon
width(25)
penup()
goto(590 , 282)
pendown()
color("silver")
forward(45)
left(200)
forward(53)
left(30)
forward(53)
right(155)
forward(40)
right(40)
forward(33)

#Stars

width(5)
penup()
goto(220,200)
pendown()
forward(3)
penup()
goto(300,190)
pendown()
forward(3)
penup()
goto(280 , 170)
pendown()
forward(3)
penup()
goto(390,300)
pendown()
forward(3)
penup()
goto(372 , 270)
penup()
goto(320 , 240)
homework="I did my best and it took 3 hour , think it was good , what do you think?"
print(homework)
exitonclick()