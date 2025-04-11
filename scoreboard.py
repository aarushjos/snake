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
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        pygame.mixer.music.stop()
        game_over=pygame.mixer.Sound(resource_path("assets/game_over.mp3"))
        game_over.play().set_volume(0.4)
        self.teleport(0,0)
        self.write("GAME OVER!",align="center",font=FONT)
        self.screen.update()
        sad_face = Turtle(resource_path("assets/sad_face.gif"))
        start_time=time.time()
        x_move=1.5
        y_move=1
        while time.time()-start_time<game_over.get_length():

            x,y=sad_face.xcor(),sad_face.ycor()
            sad_face.teleport(x+x_move,y+y_move)

            if x+x_move>290 or x+x_move<-290:
                x_move*=-1

            if y+y_move>290 or y+y_move<-290:
                y_move*=-1

            self.screen.update()
            time.sleep(0.01)
