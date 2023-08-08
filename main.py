from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()

screen.listen()
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            score.game_over()

screen.exitonclick()
