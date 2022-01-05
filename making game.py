# importing libraries
import turtle 
import random
import time

#Creating Screen
screen = turtle.Screen()
screen.title('SNAKE_GAME')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('yellow')

# Creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#Creating start button
#def printer():
#    btn=turtle.button(screen,Text='start',command=printer)
#    btn.place(x=300,y=90)

#score
score=0
delay=0.1

#snake
snake=turtle.Turtle()
snake.speed(0)
snake.color("black")
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction='stop'

#food
seed=turtle.Turtle()
seed.speed(0)
seed.shape('circle')
seed.color('red')
seed.penup()
seed.goto(30,30)

old_seed=[]

#scoring
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color('black')
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score:",align="center",font=("Times",24,"bold"))

#snake movement
def snake_go_up():
    if snake.direction != "down":
        snake.direction="up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction="down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction="left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction="right"
        
def snake_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)

    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

#keyboard using
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")

#main loop
while True:
    screen.update()
       #snake and seed colliedes
    if snake.distance(seed)<20:
        x=random.randint(-290,270)
        y=random.randint(-240,240)
        seed.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write("Score:{}".format(score),align="center",font=("Times",24,"bold"))
        delay-=0.001

        #Creating New Seed
        new_seed=turtle.Turtle()
        new_seed.speed(0)
        new_seed.shape("square")
        new_seed.color("red")
        new_seed.penup()
        old_seed.append(new_seed)

    #adding ball to snake
    for index in range(len(old_seed)-1,0,-1):
        a=old_seed[index-1].xcor()
        b=old_seed[index-1].ycor()

        old_seed[index].goto(a,b)
    
    if len(old_seed)>0:
        a=snake.xcor()
        b=snake.ycor()
        old_seed[0].goto(a,b)
    snake_move()

    #snake and border collision
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('yellow')
        scoring.goto(0,0)
        scoring.write("GAME OVER \n Your Score Is {}".format(score),align='center',font=("Times",32,'bold'))

    #snake collision
    for food in old_seed:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('yellow')
            scoring.goto(0,0)
            scoring.write("GAME OVER \n Your Score Is {}".format(score),align="center",font=("Times",30,"bold"))
            
    time.sleep(delay)

turtle.Terminator()