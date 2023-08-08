from turtle import Turtle
STARTING_POSITION = [(0, 0), (-2, 0), (-4, 0), (-6, 0)]
MOVE_FORWARD = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_segment.speed('fastest')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.my_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.my_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.my_snake) - 1, 0, -1):
            seg = self.my_snake[seg_num]
            prev_seg = self.my_snake[seg_num - 1]
            seg.goto(x=prev_seg.xcor(), y=prev_seg.ycor())
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
