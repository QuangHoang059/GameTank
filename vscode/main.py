
import pygame as pg
import numpy as np
import sys
import tank
import threading
pg.init()

fpsclock = pg.time.Clock()
fps = 90

width = 1000
height = 750
screen = pg.display.set_mode((width, height))
pg.display.set_caption("GameTank")
pg_icon = pg.image.load(".\img\cat-cupid-love-icon.png")
pg.display.set_icon(pg_icon)
font = pg.font.SysFont('Times New Roman', 20, bold=True)
# màu nền
df = pg.image.load('./img/background-nau-son.jpg')


t = tank.Tank(loaithanxe='2')

t.draw_Tank(screen)


def play():
    runing = True
    check_stop = check_up = check_dow = check_right = check_lef = False
    quantinh = 20
    while runing:
        screen.blit(df, (-30, 0))
        screen.blit(pg.Surface((20, 20)), (190, 190))
        t.update_Tank()
        quantinh = t.stop_Tank(check_stop, quantinh, check_up, check_dow)
        for even in pg.event.get():
            if even.type == pg.QUIT:
                runing = False
            elif even.type == pg.KEYDOWN:
                quantinh = 0
                check_up = check_dow = False
                if even.key == pg.K_UP or even.key == pg.K_DOWN:
                    check_stop = False
            elif even.type == pg.KEYUP:
                quantinh = 10
                if even.key == pg.K_UP:
                    check_up = True
                    check_stop = True
                elif even.key == pg.K_DOWN:
                    check_dow = True
                    check_stop = True

        t.draw_Tank(screen)
        pg.display.update()
        fpsclock.tick(fps)
    else:
        sys.exit()


play()
