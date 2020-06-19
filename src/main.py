from pygame import init, QUIT
from pygame import quit as pygame_quit
from pygame.event import get as get_events
from pygame.display import set_mode, flip
from pygame.draw import rect
from numpy.random import choice


init()


WIDTH, HEIGTH = 500, 500
SCALE = 50

COLS, ROWS = WIDTH // SCALE, HEIGTH // SCALE

grid = choice([True, False], (COLS, ROWS))

screen = set_mode((WIDTH, HEIGTH))

running = True


while running:
    for event in get_events():
        if event.type == QUIT:
            running = False

    # for x in grid:
    #     if cell:
    #         rect(screen, (255, 255, 255))
    #     else:
    #         rect(screen, (0, 0, 0))

    flip()


pygame_quit()
quit()
