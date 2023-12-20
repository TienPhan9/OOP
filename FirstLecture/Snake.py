import pygame as pg
import random

class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def window(self):
        screen = pg.display.set_mode((400, 400)) 
        return screen
    def snake(self,x,y,x_change, y_change,length, body):
        self.x = 0
        self.y = 0
        self.x_change = 200
        self.y_change = 200
        self.body = 0
        self.length = 1
    
        