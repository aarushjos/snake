import time
from mimetypes import guess_all_extensions

from food import Food
from snake import Snake
from turtle import Screen,colormode,Turtle
from scoreboard import ScoreBoard
import pygame
from utils import resource_path



#MUSIC


colormode(255)
screen=Screen()
screen.setup(width=600,height=600)
screen.bgpic(resource_path("assets/background.gif"))
screen.addshape(resource_path("assets/apple.gif"))
screen.addshape(resource_path("assets/apple_big.gif"))
screen.addshape(resource_path("assets/sad_face.gif"))
screen.title("Snakey Snake Game")

screen.tracer(0)

screen.update()
def add_new_food():
    if len(foods)<4:
        foods.append(Food(screen))
    screen.ontimer(add_new_food,2000)

screen.listen()


keypress = False

def start_game():
    global keypress
    keypress = True
    start.clear()
    start.hideturtle()

# Show start message
start = Turtle()
start.hideturtle()
start.penup()
start.goto(0, 0)
start.color("white")
start.write("Press SPACE to start", font=("Courier", 20, "bold"), align="center")

screen.onkey(start_game, "space")

# Wait until SPACE is pressed
while not keypress:

    screen.update()
    time.sleep(0.1)

snake=Snake()
scoreboard=ScoreBoard(screen)

foods=[]
initial_food=Food(screen)
foods.append(initial_food)
screen.ontimer(add_new_food,2000)
up=["Up","w","W"]
down=["Down","s","S"]
left=["Left","a","A"]
right=["Right","d","D"]
for key in up:
    screen.onkey(snake.up,key)
for key in down:
    screen.onkey(snake.down,key)
for key in left:
    screen.onkey(snake.left,key)
for key in right:
    screen.onkey(snake.right,key)

def game_loop():
    pygame.mixer.init()
    pygame.mixer.music.load(resource_path("assets/background.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    crunch_sound = pygame.mixer.Sound(resource_path("assets/crunch.mp3"))
    def game_reset(foods,snake,scoreboard):
        scoreboard.game_over(screen)
        snake.snake_reset()
        while foods:
            food = foods.pop()
            food.reset()
            food.hideturtle()

    game = True
    while game and keypress:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect food eaten
        for food in foods:
            if snake.head.distance(food) < 22:
                crunch_sound.play()
                food.goto(1000, 1000)
                foods.remove(food)
                snake.extend()
                scoreboard.increase_score()

                # If we eat the food before the timer of other one to appear at least one should be there always
                if len(foods) == 0:
                    new_food = Food(screen)
                    foods.append(new_food)

        # Detect wall collision
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game = False
            game_reset(foods,snake,scoreboard)
            game_loop()

        # Detect collision with tail
        for square in snake.squares[1:]:
            if square == snake.head:
                pass
            elif snake.head.distance(square) < 10:
                game = False
                game_reset(foods,snake,scoreboard)
                game_loop()


game_loop()


screen.exitonclick()