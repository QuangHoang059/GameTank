import pygame as pg
import numpy as np


def rotate_img(screen, img, pos, originPos, angle):
    w, h = img.get_size()
    box = [pg.math.Vector2(p)
           for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[
        0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[
        0], max(box_rotate, key=lambda p: p[1])[1])

    pivot = pg.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0],
              pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    rotated_img = pg.transform.rotate(img, angle)

    screen.blit(rotated_img, origin)
