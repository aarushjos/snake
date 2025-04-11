import random
from turtle import Turtle
from utils import resource_path

class Food(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.penup()
        #self.shapesize(stretch_len=1,stretch_wid=1) #only has affects on other shapes not .gif shapes
        self.color("red")
        self.speed("fastest")

        self.normal_shape = resource_path("assets/apple.gif")
        self.big_shape = resource_path("assets/apple_big.gif")
        self.current_shape_big = False

        self.shape(self.normal_shape)
        self.next_positions()
        self.pulse()



    def next_positions(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x,random_y)


    def pulse(self):
        if self.current_shape_big:
            self.shape(self.normal_shape)
        else:
            self.shape(self.big_shape)
        self.current_shape_big = not self.current_shape_big
        self.screen.ontimer(self.pulse, 300)