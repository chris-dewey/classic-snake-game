from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from boundary import Boundary
import time

# Screen Setup
scr = Screen()
scr.setup(width=650, height=650)
scr.bgcolor("black")
scr.title("Snake!")
scr.tracer(0)

# Initialization
snake = Snake()
food = Food()
score = Score()
boundary = Boundary()

# Get Difficulty
difficulty = scr.textinput("Difficulty", "Enter Difficulty (easy, medium, hard, very hard)")
snake.set_difficulty(difficulty)

# Listeners
scr.listen()
scr.onkey(snake.turn_north, "Up")
scr.onkey(snake.turn_south, "Down")
scr.onkey(snake.turn_west, "Left")
scr.onkey(snake.turn_east, "Right")

# Main Game
playing = True
while playing:
    # Move Snake
    scr.update()
    snake.move()
    time.sleep(snake.difficulty)

    # Eat Food (detect food collision)
    if snake.head.distance(food) < 5:
        food.new_food()
        snake.grow()
        score.increase()

    # Wall Collision Detection
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    if head_x > 300 or head_x < -300 or head_y > 300 or head_y < -300:
        score.game_over()
        playing = False

    # Tail Collision Detection
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score.game_over()
            playing = False

# Keep Screen Visible Until Exit
scr.exitonclick()
