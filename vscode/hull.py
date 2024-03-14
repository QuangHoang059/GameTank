import pygame as pg
import numpy as np
import rotate


class Hull(object):
    def __init__(self, hull, smoke):
        self.hull = hull
        self.smoke = smoke
        self.ang = 0
        self.smoke_cout = 0

    def draw_hull(self, screen, dest):
        center = (40, 51)
        self.screen = screen
        self.dest = dest
        rect_center = (center[0]+self.dest[0],
                       self.dest[1]+center[1])
        rotate.rotate_img(self.screen, self.hull,
                          rect_center, center, self.ang)

    def engine_smoke(self):
        center1 = (40, 51)
        surface_size_tack = self.hull.get_size()
        center = self.hull.get_rect().center
        rect_center = (center1[0]+self.dest[0],
                       self.dest[1]+center1[1])
        self.surface_size_smoke = (
            surface_size_tack[0], surface_size_tack[1]+10)

        smoke_surface = pg.Surface(
            self.surface_size_smoke, pg.SRCALPHA)
        smoke_surface.blit(
            self.smoke[self.smoke_cout], (center[0]-20, center[1]+10))
        rotate.rotate_img(self.screen, smoke_surface,
                          rect_center, center, self.ang)
        if self.smoke_cout <= 1:
            self.smoke_cout += 1
        else:
            self.smoke_cout = 0
