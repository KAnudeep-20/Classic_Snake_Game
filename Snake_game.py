from turtle import Turtle, Screen
import turtle as T
import time
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #this is the functon by which we can turn off the animation and by using "update()" method we can show the whole animation at once

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameis_on = True
while(gameis_on):
    screen.update()
    time.sleep(0.1)  #it delays the movement of each block by 1 second
    snake.move()

    #collision with food
    if(snake.head.distance(food) < 18):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset_snake()

    #Detect collision with tail
    for seg in snake.segment[1:]:
        if(snake.head.distance(seg)<10):
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()