from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game - Nghia Vu")

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    snake.move()
    # check food collision :
    if snake.list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()
    if snake.list[0].xcor() > 270 or snake.list[0].xcor() < -270 or snake.list[0].ycor() > 270 or snake.list[
        0].ycor() < -270:
        score.reset()
        snake.reset()

    for segment in snake.list[1:]:
        if snake.list[0].distance(segment) <= 10:
            score.reset()
            snake.reset()

screen.exitonclick()