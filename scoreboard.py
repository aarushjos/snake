import time
from turtle import Turtle
import pygame
from utils import resource_path

ALIGNMENT="center"
FONT=("Courier",15,"normal")

class ScoreBoard(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(0, 270)
        with open(resource_path("assets/data.txt")) as file:
            self.highscore=int(file.read())
        self.update_score()

    def update_score(self):
        self.goto(0,270)
        self.write(f"Score = {self.score}\tHighscore = {self.highscore}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self, screen):
        self.highscore = max(self.highscore, self.score)
        pygame.mixer.music.stop()
        game_over = pygame.mixer.Sound(resource_path("assets/game_over.mp3"))
        game_over.play().set_volume(0.3)
        restart=Turtle()
        restart.hideturtle()
        restart.penup()
        restart.goto(0,-22)
        restart.color("white")
        restart.write("(Press SPACE to restart)",align="center",font=FONT)

        self.teleport(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
        self.screen.update()

        sad_face = Turtle(resource_path("assets/sad_face.gif"))
        x_move = 1.5
        y_move = 1

        # Flag to detect space press
        self.space_pressed = False

        def handle_space():
            self.space_pressed = True

        screen.listen()
        screen.onkey(handle_space, "space")

        start_time = time.time()
        while time.time() - start_time < game_over.get_length():
            if self.space_pressed:
                game_over.stop()
                break

            x, y = sad_face.xcor(), sad_face.ycor()
            sad_face.teleport(x + x_move, y + y_move)

            if x + x_move > 290 or x + x_move < -290:
                x_move *= -1
            if y + y_move > 290 or y + y_move < -290:
                y_move *= -1

            self.screen.update()
            time.sleep(0.01)

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(0, 270)
        sad_face.reset()
        sad_face.hideturtle()
        restart.clear()
        self.clear()
        self.update_score()
        self.high_score()

    def high_score(self):
        with open(resource_path("assets/data.txt")) as data:
            prev_hs=int(data.read())
            new_hs=max(prev_hs,self.highscore)
        with open(resource_path("assets/data.txt"), mode="w") as data:
            data.write(str(new_hs))
