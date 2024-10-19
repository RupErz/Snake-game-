from turtle import Turtle
MOVE_DISTANCE = 20 #global variable
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0) , (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.list = []
        self.starting_position = [(0, 0) , (-20, 0), (-40, 0)]
        for position in self.starting_position:
            self.add_segment(position)
    
    def move(self):
        for num in range(len(self.list) - 1, 0, -1):
            x = self.list[num - 1].xcor()
            y = self.list[num - 1].ycor()
            self.list[num].goto(x, y) 
        self.list[0].forward(MOVE_DISTANCE)
        
        
    def up(self):
        if self.list[0].heading() == LEFT or self.list[0].heading() == RIGHT : 
            self.list[0].setheading(UP)
    def down(self):
        if self.list[0].heading() == LEFT or self.list[0].heading() == RIGHT : 
            self.list[0].setheading(DOWN)
    def left(self):
        if self.list[0].heading() == UP or self.list[0].heading() == DOWN : 
            self.list[0].setheading(LEFT)
    def right(self):
        if self.list[0].heading() == UP or self.list[0].heading() == DOWN : 
            self.list[0].setheading(RIGHT)
        
    def extend(self):
        #add new segment to the snake
        self.add_segment(self.list[-1].position())
    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("white")
        self.list.append(new_turtle)
    def reset(self):
        for i in self.list:
            i.goto(1000, 1000)
        self.list.clear()
        for position in self.starting_position:
            self.add_segment(position)
        
            

