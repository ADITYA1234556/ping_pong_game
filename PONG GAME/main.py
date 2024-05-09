from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scores import Scores
import time

screen = Screen()
turtle = Turtle()
screen.setup(width= 800, height= 600)
turtle.hideturtle()
screen.bgcolor("black")
screen.tracer(0)
r_paddle = (380, 0)
l_paddle = (-380, 0)
r_paddle = Paddle(r_paddle)
l_paddle = Paddle(l_paddle)
ball = Ball()
screen.listen()
screen.onkey(r_paddle.paddle_move_up, "Up")
screen.onkey(r_paddle.paddle_move_down, "Down")
screen.onkey(l_paddle.paddle_move_up, "w")
screen.onkey(l_paddle.paddle_move_down, "s")
game_on = True
r_xy = (360, 260)
r_yx = (-300, 260)
score_r = Scores(r_xy)
score_l = Scores(r_yx)
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.reset_ball()
        score_l.score += 1
        score_l.write_score()
    elif ball.xcor() < -380:
        ball.reset_ball()
        score_r.score += 1
        score_r.write_score()
#     paddle.paddle_follow()
#     paddle.paddle_follow_2()






screen.exitonclick()