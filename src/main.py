import pygame as pg


pg.init()


running = True


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()
quit()
