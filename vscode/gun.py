import numpy as np
import pygame as pg
import rotate
import bullet
import math


class Gun(object):
    def __init__(self, gun, packet_bullet) -> None:
        self.gun = gun
        self.m = np.array([0, -1])
        self.ang = None
        self.check_shoot = True
        self.packet_bullet = packet_bullet
        self.bullets = []

    def draw_gun(self, screen, dest, loai=2):
        self.loai = loai
        self.dest = dest
        self.screen = screen

        center = (40, 51)

        img = self.gun[self.loai]
        pos_mouse = np.array(pg.mouse.get_pos())
        m_d = pos_mouse-(np.array(center)+np.array(self.dest))
        # tính cos()
        cos = np.multiply(self.m, m_d) / \
            (np.linalg.norm(m_d)*np.linalg.norm(self.m))
        # đổi thành độ
        self.ang = math.degrees(math.acos(cos[-1]))
        if pos_mouse[0] > self.dest[0]+center[0]:
            self.ang = -self.ang
        self.dest = self.shoot(self.dest)
        rect_center = (center[0]+self.dest[0], self.dest[1]+center[1])

        if math.isnan(self.ang) == False:
            rotate.rotate_img(
                screen, img, rect_center, center, self.ang)

    def shoot(self, dest):
        rand = math.radians(self.ang)
        m = (math.sin(rand)*4, math.cos(rand)*4)
        muose = pg.mouse.get_pressed(num_buttons=3)
        if(muose[0] == True and self.check_shoot == True):
            self.check_shoot = False
            d = bullet.Bullet(self.packet_bullet,
                              self.screen, self.dest, self.ang)
            self.bullets.append(d)
            if len(self.bullets) > 10:
                self.bullets.pop(0)
            return (dest[0]+m[0], dest[1]+m[1])
        elif muose[0] == False and self.check_shoot == False:
            self.check_shoot = True

        return dest
