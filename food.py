from turtle import Turtle
import random
class Food(Turtle) :
    def __init__(self):
        super().__init__() #construct the parent class first 
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x = random.randint(-265, 265)
        y = random.randint(-265, 265)
        self.goto(x, y)