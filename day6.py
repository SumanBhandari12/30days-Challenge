import turtle
from turtle import Screen
tim = turtle.Turtle()
screen = Screen()
def move_forward():
        tim.forward(10)
    
def L_direction():
    tim.setheading(180)
    tim.forward(10)
    
    
def D_direction():
    tim.setheading(270)
    tim.forward(10)
    
    
def R_direction():
    tim.setheading(360)
    tim.forward(10)
    
    
def U_direction():
    tim.setheading(90)
    tim.forward(10)
 
def Clear():
    tim.reset() 


    
screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.onkey(key = "l", fun = L_direction)
screen.onkey(key = "d", fun = D_direction)
screen.onkey(key = "u", fun = U_direction)
screen.onkey(key = "r", fun = R_direction)
screen.onkey(key = "c",fun = Clear)
screen.onkey(key = "c",fun = Clear)

# for penUp and Pendown keys
def PenUP ():
    tim.penup()
    
    
def PenDown ():
    tim.pendown()

screen.onkey(key = "p", fun = PenUP)
screen.onkey(key = "P", fun = PenDown)
    
    



# screen.onkey(key = "c", fun = move_forward)





screen.exitonclick()

