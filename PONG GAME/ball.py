import random
from turtle import Turtle

turtle = Turtle()



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.ball_list = []
        # self.create_ball()
    # def ball_speed(self):
    #     self.speeding += 1
    #     print(self.speeding)
    #     self.speed(self.speeding)
    #     if self.speeding > 9:
    #         self.speeding = 0

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9



    # def ball_bounce_yr(self):
    #     new_x = self.xcor() + 10
    #     new_y = self.ycor() - 10
    #     self.goto(new_x, new_y)
    #
    # def ball_bounce_xr(self):
    #     # if self.xcor() > 380
    #     new_x = self.xcor() - 10
    #     new_y = self.ycor() - 10
    #     self.goto(new_x, new_y)
    #
    # def ball_bounce_xl(self):
    #     new_x = self.xcor() - 10
    #     new_y = self.ycor() + 10
    #     self.goto(new_x, new_y)
    #
    # def ball_bounce_yl(self):
    #     new_x = self.xcor() + 10
    #     new_y = self.ycor() + 10
    #     self.goto(new_x, new_y)
    #
    # def bounce(self):
    #     if self.ycor() > 280 and self.xcor() < 379:
    #         self.setheading(325)
    #     elif self.xcor() >= 380:
    #         self.ball_bounce_xr()
    #     elif self.ycor() < -280 and self.xcor() > -380:
    #         self.ball_bounce_xl()
    #     elif self.xcor() < -380 and self.ycor() < 280:
    #         self.ball_bounce_yl()
    # def create_ball(self):
    #     self.shape("circle")
    #     self.color("blue")
    #     self.ball_list.append(turtle)
    #     self.ball_list[0].penup()
    #     self.ball_list[0].forward(20)
    #
    # def move_ball(self):
    #     self.ball_list[0].xcor() += 20
    #     self.ball_list[0].ycor() += 20
