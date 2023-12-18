import pygame as pg
import random
#window game
screen = pg.display.set_mode((400,400))
pg.display.set_caption('Snake game')

#snake
snake_part = 20 
x = 200
y = 200
x_change=0
y_change=0
body = []
length = 1
#food
food_x = random.randint(0,19)* snake_part
food_y = random.randint(0,19)* snake_part

#speed
clock = pg.time.Clock()
speed = 3

#game play
game_play = True
while True:
    for event in pg.event.get():
        #Quit
        if event.type == pg.QUIT:
            pg.quit()
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT: # qua trai
                x_change = x_change - snake_part
                y_change = 0
            if event.key == pg.K_LEFT: # qua trai
                x_change = x_change - snake_part
                y_change = 0
            if event.key == pg.K_LEFT: # qua trai
                x_change = x_change - snake_part
                y_change = 0
            if event.key == pg.K_LEFT: # qua trai
                x_change = x_change - snake_part
                y_change = 0           
            
    #update screen
    pg.display.update()