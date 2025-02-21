import turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        t = turtle.Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            self.segments[x].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

