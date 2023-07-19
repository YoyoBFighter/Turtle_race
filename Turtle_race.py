from turtle import *
from random import randint



speed(0)
penup()

#tracing track

goto(-140,140)

    
for step in range(15):
    write(step,align="center")
    right(90)

    for num in range(8):
        penup()
        fd(10)
        pendown()
        fd(10)

    penup()
    backward(160)
    left(90)
    forward(20)    


player_1=Turtle()
player_1.shape("turtle")
player_1.pencolor("red")
player_1.penup()
player_1.goto(-140,120)    
player_1.pendown()
for turn in range(10):
    player_1.lt(36)

player_2=Turtle()
player_2.shape("turtle")
player_2.pencolor("blue")
player_2.penup()
player_2.goto(-140,100)
player_2.pendown()
for turn in range(5):
    player_2.rt(72)

player_3=Turtle()
player_3.shape("turtle")
player_3.pencolor("cyan")
player_3.penup()
player_3.goto(-140,80)
player_3.pendown()
for turn in range(40):
    player_3.lt(9)

player_4=Turtle()
player_4.shape("turtle")
player_4.pencolor("green")
player_4.penup()
player_4.goto(-140,60)
player_4.pendown()
for turn in range(20):
    player_4.rt(18)

for turn in range(100):
    player_1.fd(randint(1,5))    
    player_2.fd(randint(1,5))  
    player_3.fd(randint(1,5))  
    player_4.fd(randint(1,5))  


mainloop()