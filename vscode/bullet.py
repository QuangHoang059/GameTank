import pygame as pg
import numpy as np
import rotate
import math


class Bullet(object):
    def __init__(self, img_packet_bullet, screen, dest, ang):
        self.img_packet_bullet = img_packet_bullet
        self.cout = 0
        self.screen = screen
        self.dest = np.array(dest)
        self.ang = ang
        self.flightiness = 60
        self.check_hide = True

    def draw_bullet_path(self):
        self.show = self.img_packet_bullet[self.cout]
        rect = self.show.get_rect()
        center1 = (rect.center[0], rect.center[1])
        post = (self.dest[0]+center1[0]+20,
                self.dest[1]+center1[1]+rect[3]-10)
        if self.check_hide == True:
            if self.cout == 0:
                rotate.rotate_img(self.screen, self.show,
                                  post, center1, self.ang)
            else:
                post = (self.dest[0]+center1[0],
                        self.dest[1]+center1[1]+5)
                rotate.rotate_img(self.screen, self.show,
                                  post, center1, self.ang)

    def move(self):
        if self.flightiness > 0:
            rand = math.radians(self.ang)
            xy = np.array((math.sin(rand)*5, math.cos(rand)*5))
            self.dest -= xy

        self.flightiness -= 0.75
        if self.flightiness < 10:
            if self.cout < 8:
                self.cout += 1
        if self.flightiness < 0:
            self.check_hide = False
