from pygame import *
from cube import Cube
import sys

WIDTH, HEIGHT = 700, 700

screen = display.set_mode((WIDTH, HEIGHT))

cube = Cube(screen)

while True:
    screen.fill((0,0,0))

    cube.draw()

    for ev in event.get():
        if ev.type == QUIT:sys.exit()
        if ev.type == KEYDOWN:
            image.save(screen, "ss.png")
    
    display.update()
    clock = time.Clock()
    clock.tick(clock.get_fps())