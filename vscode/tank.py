import getdata
import track
import hull
import gun
import pygame as pg
import numpy as np
import math


class Tank(object):
    def __init__(self, speed=0.15, mauxe='A', loaithanxe='1', loaixung='1', loaixich='1'):
        img_hull, img_gun, img_track, img_tire_track, img_smoke, img_packet_bullet = getdata.get_tank(
            mauxe, loaithanxe, loaixung, loaixich)
        # thư viện sử lí tất cả hiệu ứng thân máy
        self.img_hull = hull.Hull(img_hull, img_smoke)
        # thư viện sử lí súng và đạn bắn ra
        self.img_gun = gun.Gun(img_gun, img_packet_bullet)
        # thư viện track bao gồm cả track và tire track
        self.speed = speed
        self.img_track = track.Track(img_track, img_tire_track, self.speed)
        self.rect_tank = np.array([50., 50.])
        self.ang = 0
        self.huong = np.array((math.sin(self.ang)*self.speed,
                              math.cos(self.ang)*self.speed))

    def draw_Tank(self, screen):
        self.screen = screen
        surface_size_tack = self.img_hull.hull.get_size()
        self.img_track.draw_track(
            screen, surface_size_tack, self.rect_tank, 68, 2, 1)
        self.img_hull.draw_hull(screen, self.rect_tank)

        for i in self.img_gun.bullets:
            i.draw_bullet_path()
            i.move()
        self.img_gun.draw_gun(screen, self.rect_tank)

    def speed_up(self):
        if(self.speed < 1.5):
            self.speed += 0.0085

    def set_ang(self):
        self.img_hull.ang = self.ang
        self.img_track.ang = self.ang

    def update_Tank(self):
        phim = pg.key.get_pressed()
        if phim[pg.K_UP] and phim[pg.K_RIGHT]:
            self.rect_tank -= self.huong
            self.ang -= 0.75
            self.speed_up()
            self.set_ang()
            self.img_track.draw_track_tire(68, 50, self.speed, 1, 2)
            self.img_hull.engine_smoke()
            self.img_track.update_up(1)
        elif phim[pg.K_UP] and phim[pg.K_LEFT]:
            self.rect_tank -= self.huong
            self.ang += 0.75
            self.speed_up()
            self.set_ang()
            self.img_track.draw_track_tire(68, 50, self.speed, 1, 1)
            self.img_hull.engine_smoke()
            self.img_track.update_up(2)
        elif phim[pg.K_DOWN] and phim[pg.K_RIGHT]:
            self.rect_tank += self.huong
            self.ang -= 0.75
            self.speed_up()
            self.set_ang()
            self.img_track.draw_track_tire(68, 50, self.speed, 1, 2, huong=1)
            self.img_hull.engine_smoke()
            self.img_track.update_dow(1)
        elif phim[pg.K_DOWN] and phim[pg.K_LEFT]:
            self.rect_tank += self.huong
            self.ang += 0.75
            self.speed_up()
            self.set_ang()
            self.img_hull.engine_smoke()
            self.img_track.draw_track_tire(68, 50, self.speed, 1, 1, huong=1)
            self.img_track.update_dow(2)
        elif phim[pg.K_UP]:
            self.rect_tank -= self.huong
            self.speed_up()
            self.img_track.draw_track_tire(68, 50, self.speed, 1)
            self.img_hull.engine_smoke()
            self.img_track.update_up()
        elif phim[pg.K_RIGHT]:
            self.ang -= 1
            self.set_ang()
            self.img_track.update_rotate(0)
        elif phim[pg.K_LEFT]:
            self.ang += 1
            self.set_ang()
            self.img_track.update_rotate(1)
        elif phim[pg.K_DOWN]:
            self.rect_tank += self.huong
            self.speed_up()
            self.img_track.draw_track_tire(68, 50, self.speed, 1, huong=1)
            self.img_hull.engine_smoke()
            self.img_track.update_dow()
        if(abs(self.ang) >= 360):
            self.ang = 0
        radius = math.radians(self.ang)
        self.huong = np.array((math.sin(radius)*self.speed,
                               math.cos(radius)*self.speed))

    def stop_Tank(self, check_stop, quantinh, check_up, check_dow):
        if check_stop == True:
            if self.speed > 0.15:
                self.speed -= 0.0085
        if quantinh >= 0:
            if check_up == True:
                self.rect_tank -= self.huong
            elif check_dow == True:
                self.rect_tank += self.huong
            quantinh -= 1
        return quantinh
