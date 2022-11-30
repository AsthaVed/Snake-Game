# import required modules
import turtle
import time
import random
  
delay = 0.1
score = 0
high_score = 0 

#snakebodies
bodies=[]
  
# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("gray")
# the width and height can be put as user's choice
wn.setup(width=700, height=600)
wn.tracer(0)
  
# head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.shapesize(1,1,2)   
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
  
# food in the game
food = turtle.Turtle()
colors = random.choice(['orange', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.hideturtle()
food.goto(0, 100)
food.showturtle()
  
#score board  
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.fillcolor("black")
pen.penup()
pen.hideturtle()
pen.goto(-10, -250)
pen.write("Score : 0  |  High Score : 0", align="center", font=("candara", 24, "bold"))
  

# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up" 
  
def godown():
    if head.direction != "up":
        head.direction = "down" 
  
def goleft():
    if head.direction != "right":
        head.direction = "left"  
  
def goright():
    if head.direction != "left":
        head.direction = "right"

def gostop():
    head.direction = "stop"  
  
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# event handling         
wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(gostop, "space")
  
  
# Main Gameplay
while True:
    wn.update()  #this is to update the screen
    #check collission with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    #check collision with food
    if head.distance(food) < 20:
        # move the food to new random place
        x = random.randint(-290, 290)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # increase the length othe snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)          # append new body

        # increase the score
        score += 10

        # change delay
        delay -= 0.001

        # update the heighest score
        if score>high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # move the snake body
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)
    
    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
    move()

    # check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide bodies
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            score=0
            delay=0.1

            #update score board
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
wn.mainloop()