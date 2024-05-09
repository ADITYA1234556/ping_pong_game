from turtle import Turtle
POSITIONS = [(-380, 0), (-380,-20), (-380,20)]
POSITIONS_2= [(380, 0), (380,-20), (380,20)]
COLORS = ["red", "blue", "green"]
MOVE = 20
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
