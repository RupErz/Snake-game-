from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', mode ="r") as fout :
            self.high_score = int(fout.read()) #take the updated data everytime we run
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 260)
        self.pen(shown = False, pensize = 100)
        self.write_score()
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.high_score}", False, ALIGNMENT, FONT)
    def add_score(self):
        self.score += 1
        self.write_score()
    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER", False, ALIGNMENT, FONT)
    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open('data.txt', mode ="w") as fout :
                fout.write(str(self.high_score))
            self.score = 0
            self.write_score()
        
        