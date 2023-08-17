from pygame import Surface, draw
import math
from numpy import matmul
import numpy as np
from pygame.font import Font, get_default_font, init
init()

class Cube:
    linePos = {
        "4": 7,
        "5": 2,
        "6": 1,
        "7": 0
    }
    angle = 0
    font = Font(get_default_font(), 30)
    def __init__(self, screen:Surface, size=50):
        self.size = size
        self.screen = screen
        self.points = np.zeros([8, 3])
        self.points[0] = [-50, -50, -50]
        self.points[1] = [-50, 50, -50]
        self.points[2] = [50, 50, -50]
        self.points[3] = [50, -50, -50]
        self.points[7] = [-50, -50, 50]
        self.points[6] = [-50, 50, 50]
        self.points[5] = [50, 50, 50]
        self.points[4] = [50, -50, 50]

        self.proj = np.zeros([3, 3])
        self.proj[0] = [1, 0, 0]
        self.proj[1] = [0, 1, 0]
        self.proj[2] = [0, 0, 0]

    def draw(self):
        center = [
            self.screen.get_width()/2-self.size/2,
            self.screen.get_height()/2-self.size/2
        ]

        rotationZ = np.zeros([3, 3])
        rotationZ[0] = [math.cos(self.angle), -math.sin(self.angle), 0]
        rotationZ[1] = [math.sin(self.angle), math.cos(self.angle), 0]
        rotationZ[2] = [0, 0, 1] 

        rotationX = np.zeros([3, 3])
        rotationX[0] = [1, 0, 0]
        rotationX[1] = [0, math.cos(self.angle), -math.sin(self.angle)]
        rotationX[2] = [math.sin(self.angle), math.cos(self.angle), 0]

        rotationY = np.zeros([3, 3])
        rotationY[0] = [math.cos(self.angle), 0, -math.sin(self.angle)]
        rotationY[1] = [0, 1, 0]
        rotationY[2] = [math.sin(self.angle), 0, math.cos(self.angle)]

        def rotate(pos):
            rotated = matmul(rotationY, pos)
            rotated = matmul(rotationX, rotated)
            rotated = matmul(rotationZ, rotated)
            proj2D = matmul(self.proj, rotated)
            pos = [
                center[0]+proj2D[0],
                center[1]+proj2D[1]
            ]
            return pos

        here = 0
        for pos in self.points:
            pos = rotate(pos)

            draw.circle(
                self.screen,
                (200, 0, 200),
                pos, 15
            )

            if here != 0:
                endpos = rotate(self.points[here-1])
                draw.line(
                    self.screen,
                    (200, 0, 200),
                    pos, endpos
                )

            #if here > self.points.__len__()/2-1:
                #draw.line(
                #    self.screen,
                #    (200, 0, 200),
                #    pos, rotate(self.points[here-3])
                #)

            if str(here) in self.linePos:
                draw.line(
                    self.screen,
                    (200, 0, 200),
                    pos, rotate(self.points[self.linePos[str(here)]])
                )

            if here == 3:
                draw.line(
                    self.screen,
                    (200, 0, 200),
                    pos, rotate(self.points[0])
                )

            here += 1
        
        self.angle += 0.001