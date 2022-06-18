from turtle import Turtle
MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.difficulty = 0.3 # Default Difficulty "easy"
        self.new_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.current_direction = EAST

    def new_snake(self):
        for i in range(3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.goto(i * -20, 0)
            segment.color("white")
            self.segments.append(segment)

    def grow(self):
        new_x = self.tail.xcor()
        new_y = self.tail.ycor()
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)

    def turn_north(self):
        if self.current_direction != SOUTH:
            self.head.setheading(NORTH)

    def turn_south(self):
        if self.current_direction != NORTH:
            self.head.setheading(SOUTH)

    def turn_east(self):
        if self.current_direction != WEST:
            self.head.setheading(EAST)

    def turn_west(self):
        if self.current_direction != EAST:
            self.head.setheading(WEST)

    def set_difficulty(self, new_difficulty):
        match new_difficulty.lower():
            case "easy":
                self.difficulty = 0.3
            case "medium":
                self.difficulty = 0.2
            case "hard":
                self.difficulty = 0.125
            case "very hard":
                self.difficulty = 0.1

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)
        self.current_direction = self.head.heading()




