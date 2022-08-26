from turtle import Screen
from paddle import *
from score import Score
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1400, height=800)
screen.title("Pong Game")
screen.tracer(0)

main_turtle = Turtle()
main_turtle.penup()
main_turtle.color("white")
main_turtle.pensize(3)
main_turtle.setposition(0, 400)
main_turtle.setheading(270)
while main_turtle.ycor() != -400:
    main_turtle.pendown()
    main_turtle.forward(10)
    main_turtle.penup()
    main_turtle.forward(10)

l_paddle = Paddle((-680, 0))
r_paddle = Paddle((670, 0))
l_score = Score((-130, 280))
r_score = Score((70, 280))
ball = Ball()


screen.listen()
screen.onkey(l_paddle.on_up, key="a")
screen.onkey(l_paddle.on_down, key="s")
screen.onkey(r_paddle.on_up, key="Up")
screen.onkey(r_paddle.on_down, key="Down")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    if not -370 <= ball.ycor() <= 380:
        ball.bounce_y()

    if ball.distance(l_paddle) < 60 and ball.xcor() < -650:
        ball.bounce_x()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 640:
        ball.bounce_x()

    if ball.xcor() >= 705:
        l_score.increase_score()
        ball.refresh()

    if ball.xcor() <= -705:
        r_score.increase_score()
        ball.refresh()

screen.exitonclick()
