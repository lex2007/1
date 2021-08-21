import turtle
from turtle import *
from random import randrange
import time
BREAK_FLAG = False





yo = turtle.Screen()
yo.title('yama')
yo.setup(650, 650, 650, 650)
yo.tracer(0)

border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)

snake = []
for i in range(3):
    snake_segment = turtle.Turtle()
    snake_segment.shape('circle')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('gray')
    snake.append(snake_segment)

food = turtle.Turtle()
food.shape('circle')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

yo.onkeypress(lambda: snake[0].setheading(90), 'Up')
yo.onkeypress(lambda: snake[0].setheading(270), 'Down')
yo.onkeypress(lambda: snake[0].setheading(0), 'Right')
yo.onkeypress(lambda: snake[0].setheading(180), 'Left')
yo.listen()

while True:
    if snake[0].distance(food) < 10:
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('circle')
        snake_segment.color('grey')
        snake_segment.penup()
        snake.append(snake_segment)

    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    snake[0].forward(20)

    yo.update()
    time.sleep(0.1)

    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()
    if x_cor > 300 or x_cor < -300:
        yo.bgcolor('red')
        break
    if y_cor > 300 or y_cor < -300:
        yo.bgcolor('red')
        break

    for i in snake[1:]:
        i = i.position()
        if snake[0].distance(i)<10:
            BREAK_FLAG = True
        if BREAK_FLAG:
            yo.bgcolor('red')
            break




yo.mainloop()
