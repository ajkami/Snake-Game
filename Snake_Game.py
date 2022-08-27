#imports
from hashlib import new
import turtle
import time
import random

delay = 0.1

#Setting up screen
screen = turtle.Screen()
screen.title("Snake game")
screen.bgcolor("blue")
screen.setup(width=600, height=600)
screen.tracer(0) #turns off screen update

#Score writer

#snake head 
head = turtle.Turtle() #(turtle is like pointer)
head.speed(0)#setting speed to 0 gives fastest animation speed
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0) # Placing head in the middle of the screen
head.direction = "stop"

segments = []

#Snake food
food = turtle.Turtle() #(turtle is like pointer)
food.speed(0)#setting speed to 0 gives fastest animation speed
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100) # Placing head in the middle of the screen


#Functions
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_right():
    head.direction = "right"
    
def go_left():
    head.direction = "left"
    

def move():
    if head.direction == "up":
        y = head.ycor() #gets the heads current y position
        head.sety(y + 20) #moves the head by 20 upwards
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
# Key binds
screen.listen() #makes window listen to keypress
screen.onkeypress(go_up,"w") #set the function that will run when you input a certain key
screen.onkeypress(go_down,"s")
screen.onkeypress(go_right,"d")
screen.onkeypress(go_left,"a")
        

score = 0 #setting score var to add to 
#Main game loop (while true loop keeps going)
while True:
    screen.update() #screen constantly updates
      
    # See if head collides with food
    if head.distance(food) < 20:
        #Move food to random position
        score+=1 
        print("Score: " + str(score))
        x = random.randint(-290,290) #Random x position
        y = random.randint(-290,290) #Random y position
        food.goto(x,y)
        
        #Add a segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    # Move segment 0 to head position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
                
    move()# moving head based off of keypress
    time.sleep(delay) #gives a delay of 0.1 seconds for the screen during each loop

#This makes the window stay open
screen.mainloop()