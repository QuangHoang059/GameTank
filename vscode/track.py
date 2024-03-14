import pygame as pg
import numpy as np
import rotate


class Track(object):
    def __init__(self, track, tire_track, speed=0.15) -> None:
        self.track_left = track
        self.track_right = track
        self.tire_track = tire_track
        self.ang = 0
        self.cout_tracklr = 0
        self.speed = speed
        self.yl = 0
        self.yr = 0

    def create_face_lr(self):
        loai2 = 1-self.loai
        surface_track_l = pg.Surface(self.size_track, pg.SRCALPHA)
        surface_track_r = pg.Surface(self.size_track, pg.SRCALPHA)

        surface_track_l.blit(self.track_left[self.loai], (0, self.yl))
        surface_track_l.blit(
            self.track_left[loai2], (0, self.yl+self.size_track[1]))
        surface_track_l.blit(
            self.track_left[self.loai], (0, self.yl-self.size_track[1]))

        surface_track_r.blit(self.track_right[self.loai], (0,  self.yr))
        surface_track_r.blit(
            self.track_right[loai2], (0,  self.yr + self.size_track[1]))
        surface_track_r.blit(
            self.track_right[self.loai], (0,  self.yr - self.size_track[1]))
        return surface_track_l, surface_track_r

    def update_up(self, lr=0):
        if lr == 0:
            self.yl -= self.speed
            if self.yl < -self.size_track[1]:
                self.yl += self.size_track[1]
            self.yr = self.yl
        elif lr == 1:
            self.yl -= self.speed
            if self.yl < -self.size_track[1]:
                self.yl += self.size_track[1]
        elif lr == 2:
            self.yr -= self.speed
            if self.yr < -self.size_track[1]:
                self.yr += self.size_track[1]

    def update_dow(self, lr=0):
        if lr == 0:
            self.yl += self.speed
            if self.yl > self.size_track[1]:
                self.yl -= self.size_track[1]
            self.yr = self.yl
        elif lr == 1:
            self.yl += self.speed
            if self.yl > self.size_track[1]:
                self.yl -= self.size_track[1]
        elif lr == 2:
            self.yr += self.speed
            if self.yr > self.size_track[1]:
                self.yr -= self.size_track[1]

    def update_rotate(self, lr=0):
        if lr == 0:
            self.yl -= self.speed
            if self.yl < -self.size_track[1]:
                self.yl += self.size_track[1]
            self.yr += self.speed
            if self.yr > self.size_track[1]:
                self.yr -= self.size_track[1]
        elif lr == 1:
            self.yr -= self.speed
            if self.yr < -self.size_track[1]:
                self.yr += self.size_track[1]
            self.yl += self.speed
            if self.yl > self.size_track[1]:
                self.yl -= self.size_track[1]

    def draw_track(self, screen, surface_size_tack, dest, distance_lr, trucy, loai=0):
        center1 = (40, 51)
        self.screen = screen
        self.dest = dest
        self.surface_size_tack = surface_size_tack
        rect_center_track = (center1[0]+self.dest[0],
                             self.dest[1]+center1[1])
        self.loai = loai
        track_surface = pg.Surface(self.surface_size_tack, pg.SRCALPHA)
        rect_track = track_surface.get_rect()
        center_track = rect_track.center
        self.size_track = self.track_right[0].get_size()
        rect_left = (center_track[0]-distance_lr/2, trucy)
        rect_right = (center_track[0]+distance_lr/2 -
                      self.size_track[0], trucy)
        surface_track_l, surface_track_r = self.create_face_lr()
        track_surface.blit(surface_track_l, rect_left)
        track_surface.blit(surface_track_r, rect_right)
        rotate.rotate_img(self.screen, track_surface,
                          rect_center_track, center1, self.ang)

    def draw_track_tire(self, distance_lr, trucy, speed, loai=0, lef_righ=0, huong=0):
        center1 = (40, 51)
        if huong == 1:
            trucy += 27
        rect_center_track_tire = (center1[0]+self.dest[0],
                                  self.dest[1]+center1[1])
        self.surface_size_tack_tire = (
            self.surface_size_tack[0], self.surface_size_tack[1]+40)

        track_tire_surface = pg.Surface(
            self.surface_size_tack_tire, pg.SRCALPHA)

        rect_track_tire = track_tire_surface.get_rect()
        cente_tirer = rect_track_tire.center
        rect_left_tire = None
        rect_right_tire = None
        if lef_righ == 0:
            rect_left_tire = (cente_tirer[0]-distance_lr/2-13, trucy+speed*15)
            rect_right_tire = (cente_tirer[0]+distance_lr/2 - 13 -
                               self.track_right[0].get_width(), trucy+speed*15)
        elif lef_righ == 1:
            rect_left_tire = (cente_tirer[0]-distance_lr/2-13, trucy+speed*7)
            rect_right_tire = (cente_tirer[0]+distance_lr/2 - 13 -
                               self.track_right[0].get_width(), trucy+speed*15)
        elif lef_righ == 2:
            rect_left_tire = (cente_tirer[0]-distance_lr/2-13, trucy+speed*15)
            rect_right_tire = (cente_tirer[0]+distance_lr/2 - 13 -
                               self.track_right[0].get_width(), trucy+speed*7)
        track_tire_surface.blit(self.tire_track[loai], rect_left_tire)
        track_tire_surface.blit(self.tire_track[loai], rect_right_tire)
        if huong == 0:
            rotate.rotate_img(
                self.screen, track_tire_surface, rect_center_track_tire, center1, self.ang)
        elif huong == 1:
            rotate.rotate_img(
                self.screen, track_tire_surface, rect_center_track_tire, center1, self.ang+180)
