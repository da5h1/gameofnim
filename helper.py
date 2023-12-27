import numpy as np

WIDTH = 600
HEIGHT = 650
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREY = (128,128,128)
RADIUS = 15
OUTLINE = 8

def pos_on_button(pos):
    x,y = pos
    return x>=30 and x<=90 and y>=400 and y<=460

def dist(x1,y1,x2,y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)
