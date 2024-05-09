from turtle import Turtle
class Scores(Turtle):
    def __init__(self, positionz):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(positionz)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg= f"Score: {self.score}", align= "right", font= ("courier", 14, "normal"))
