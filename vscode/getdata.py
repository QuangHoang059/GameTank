import os
import pygame as pg


def _setsizeimg(p, tl=3.2):
    rectt = p.get_size()
    p = pg.transform.scale(p, (rectt[0]/tl, rectt[1]/tl))
    return p


def get_tank(mauxe='A', loaithanxe='1', loaixung='1', loaixich='1'):
    path = 'craftpix-901177-free-2d-battle-tank-game-assets/PNG/'
    # lấy thân xe
    hulls = 'Hulls_Color_'+mauxe
    hull = '/Hull_0'+loaithanxe+'.png'
    imghull = pg.image.load(path+hulls+hull)
    imghull = _setsizeimg(imghull)
    # lấy xúng xe
    arr = ['_A', '_B', '']
    img_gun = []
    weapon = 'Weapon_Color_'+mauxe+'_256X256'
    for i in arr:
        gun = '/Gun_0'+loaixung+i+'.png'
        p = pg.image.load(path+weapon+gun)
        p = _setsizeimg(p)
        img_gun.append(p)
    # lấy bánh xe
    img_track = []
    for i in range(2):
        track = 'Tracks/Track_'+loaixich+arr[i]+'.png'
        p = pg.image.load(path+track)
        p = _setsizeimg(p)
        img_track.append(p)
    # lấy vệt xe đi qua
    img_tire_track = []
    for i in range(1, 3):
        tire = 'Effects/Tire_Track_0'+str(i)+'.png'
        p = pg.image.load(path+tire)
        p = _setsizeimg(p)
        img_tire_track.append(p)
    # lấy khói xe
    img_smoke = []
    for i in range(3):
        tire = 'Effects/Smoke_'+chr(65+i)+'.png'
        p = pg.image.load(path+tire)
        p = _setsizeimg(p)
        img_smoke.append(p)
    # lấy đạn và hiệu ứng nổ của đạn
    img_packet_bullet = []
    img_packet_bullet.append(_setsizeimg(
        pg.image.load(path+'Effects/Medium_Shell.png')))
    for i in range(8):
        tire = 'Effects/Explosion_'+chr(65+i)+'.png'
        p = pg.image.load(path+tire)
        p = _setsizeimg(p)
        img_packet_bullet.append(p)
    return imghull, img_gun, img_track, img_tire_track, img_smoke, img_packet_bullet
