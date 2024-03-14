import getdata
import pygame as pg
import sys
pg.init()

fpsclock = pg.time.Clock()
fps = 90

width = 1000
height = 800
screen = pg.display.set_mode((width, height))
df = pg.image.load('./img/background-nau-son.jpg')
img_hull, img_gun, img_track, img_tire_track = getdata.get_tank()

img = img_hull.convert()


def rotate_gun(screen, img, pos, originPos, angle):

    w, h = img.get_size()
    box = [pg.math.Vector2(p)
           for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[
        0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[
        0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pg.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated img
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0],
              pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated img
    rotated_img = pg.transform.rotate(img, angle)

    # rotate and blit the img
    screen.blit(rotated_img, origin)


def play():
    angle = 0
    while True:
        angle += 3

        # Background --------------------------------------------- #
        screen.fill((0, 50, 0))
        rotate_gun(screen, img, (90, 90), (40, 40), angle)
        # mx, my = pg.mouse.get_pos()
        # img_copy = pg.transform.rotate(img, angle)
        # screen.blit(img_copy, (mx - int(img.get_width() / 2),
        #             my - int(img.get_height() / 2)))

        # Buttons ------------------------------------------------ #
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

        # Update ------------------------------------------------- #
        pg.display.update()
        fpsclock.tick(60)


play()
