from pygame import init, QUIT
from pygame import quit as pygame_quit
from pygame.event import get as get_events
from pygame.display import set_mode, flip
from pygame.draw import rect
from numpy.random import choice


init()


WIDTH, HEIGTH = 500, 500
SCALE = 10
OUTLINE_FACTOR = 0.8
COLS = WIDTH // SCALE
ROWS = HEIGTH // SCALE

grid = choice([True, False], (COLS, ROWS))

screen = set_mode((WIDTH, HEIGTH))

running = True


while running:
    for event in get_events():
        if event.type == QUIT:
            running = False

    for x in range(COLS):
        for y in range(ROWS):
            if grid[x, y]:
                rect(
                    screen,
                    (255, 255, 255),
                    (
                        x * SCALE,
                        y * SCALE,
                        int(SCALE * OUTLINE_FACTOR),
                        int(SCALE * OUTLINE_FACTOR)
                    )
                )

    flip()


pygame_quit()
quit()
