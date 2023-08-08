from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.count_score = 0
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg="Score = 0", move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.count_score += 1
        self.write(arg=f"Score = {self.count_score}", move=False, align='center', font=("Arial", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=False, align='center', font=("Arial", 15, "normal"))
        self.goto(0, -100)
        self.write(arg=f"Final Score = {self.count_score}", move=False, align='center', font=("Arial", 15, "normal"))
