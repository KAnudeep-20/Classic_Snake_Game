from turtle import Turtle, Screen
import turtle as T
import random, time

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        #CREATING SNAKE BODY
        self.segment = []
        self.create_snake()
    
    def create_snake(self):
        for pos in starting_pos:
            self.add_segment(pos)
        self.head  = self.segment[0]

    def add_segment(self, pos):
        #ADDING A NEW SEGMENT TO SNAKE BODY
        new_segment = Turtle("square")
        print(new_segment)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment.append(new_segment)
    
    def reset_snake(self):  #Here the previous snake will be cleared and a new sanke is created
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.segment[-1].position())  #Here the segmenty[-1] refers to the last box of which want to add as extension to snake after eating food

    def move(self):
        #MOVING THE SNAKE
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)
