from turtle import Turtle , Screen, down
import random
tim = Turtle()
tim.shape("circle")
tim.hideturtle()
# tim.width(10)
tim.speed('fastest')
tim.clear()

colors = ["red","green","blue","yellow","pink"]
for i in range(50):
    
    tim.forward(5)
    tim.penup()
    tim.forward(2)
    tim.pendown()
    tim.forward(5)

for i in range(4):
    tim.color(random.choice(colors))
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    
for i in range(5):
    tim.color(random.choice(colors))
    tim.forward(100)
    tim.left(72)
    tim.forward(100)
    
for i in range(6):
    tim.color(random.choice(colors))
    tim.forward(100)
    tim.left(60)
    tim.forward(100)
    
    
for i in range(7):
    tim.color(random.choice(colors))
    tim.forward(100)
    tim.left(51.428)
    tim.forward(100)
    
def draw(numOfSides): 
        angle = 360 % numOfSides 
        for i in range(numOfSides):
            tim.forward(50)
            tim.right(angle)
            
for sides in range(4,11):
    draw(sides)
    print(sides)


numbers = []
for i in range(360):
    numbers.append(i)
    
print(numbers)
sides = [0,90,150,120,69]

for i in range(50000):
    tim.color(random.choice(colors))
    tim.forward(.1)
    tim.setheading(random.choice(sides))
    
for i in range(500):
    tim.circle(100)
    tim.setheading(tim.heading() + 5)

for i in range(30):
    
    tim.dot(20,"red")
    tim.forward(10)
    
# 270 -down
# 90 -up
# 180 -left

tim.forward(100)
tim.setheading(270)
tim.forward(100)


tim.setheading(210)
tim.forward(280)

tim.setheading(360)
for i in range(20):
    tim.dot(10, "green")
    tim.forward(20)



screen = Screen()
screen.exitonclick()

