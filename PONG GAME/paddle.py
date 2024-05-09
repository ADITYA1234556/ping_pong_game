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
    # def create_paddle_1(self):
    #
    #
    #
    # def paddle_move_up(self):
    #
    #     self.setheading(90)


    # def create_paddle_1(self):
    #     for data in range(3):
    #         turtle = Turtle("square")
    #         turtle.color(COLORS[data])
    #         turtle.penup()
    #         turtle.goto(POSITIONS[data])
    #         self.paddle_block.append(turtle)
    #
    # def create_paddle_2(self):
    #     for data_2 in range(3):
    #         turtle = Turtle("square")
    #         turtle.color(COLORS[data_2])
    #         turtle.penup()
    #         turtle.goto(POSITIONS_2[data_2])
    #         self.paddle_block_2.append(turtle)
    #
    # def paddle_move_r_up(self):
    #     self.paddle_block_2[0].setheading(90)
    #
    # def paddle_move_r_down(self):
    #     self.paddle_block_2[0].setheading(270)
    #
    # def paddle_follow_2(self):
    #     for follow in range(len(self.paddle_block_2) - 1, 0, -1):
    #         x_pos = self.paddle_block_2[follow - 1].xcor()
    #         y_pos = self.paddle_block_2[follow - 1].ycor()
    #         self.paddle_block_2[follow].goto(x_pos, y_pos)
    #     self.paddle_block_2[0].forward(MOVE)
    # def paddle_move_up(self):
    #     self.paddle_block[0].setheading(90)
    #
    # def paddle_move_down(self):
    #     self.paddle_block[0].setheading(270)
    #
    # def paddle_follow(self):
    #     for follow in range(len(self.paddle_block) - 1, 0, -1):
    #         x_pos = self.paddle_block[follow - 1].xcor()
    #         y_pos = self.paddle_block[follow - 1].ycor()
    #         self.paddle_block[follow].goto(x_pos, y_pos)
    #     self.paddle_block[0].forward(MOVE)