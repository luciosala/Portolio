from turtle import* 
from random import randint 
bgcolor('blue') 
y = randint(1, 255)

pencolor(randint, randint, randint )
x = 1 
speed(0) 
while(True):
    fd(x+10)
    right(30)
    x += 3
    right(30)
    x += 3
exitonclick()