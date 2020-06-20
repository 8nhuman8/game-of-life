from pygame import init, QUIT
from pygame import quit as pygame_quit
from pygame.event import get as get_events
from pygame.display import set_mode, set_caption
from pygame.display import flip
from pygame.draw import rect
from pygame.time import Clock

from numpy import zeros
from numpy.random import choice


init()
set_caption('Game of Life')


WIDTH, HEIGTH = 500, 500
SCALE = 10
OUTLINE_FACTOR = 0.8
COLS = WIDTH // SCALE
ROWS = HEIGTH // SCALE

grid = choice([True, False], (COLS, ROWS))

screen = set_mode((WIDTH, HEIGTH))
clock = Clock()

running = True


def count_neighbors(grid, x, y):
    sum = -int(grid[x, y])
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (x + i + COLS) % COLS
            row = (x + j + ROWS) % ROWS
            sum += int(grid[col, row])
    return sum

def next_generation(grid):
    next = zeros((COLS, ROWS), bool)
    for x in range(COLS):
        for y in range(ROWS):
            state = grid[x, y]
            neighbors = count_neighbors(grid, x, y)
            if not state and neighbors == 3:
               next[x, y] = True
            elif state and (neighbors < 2 or neighbors > 3):
               next[x, y] = False
            else:
               next[x, y] = state
    return next


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

    grid = next_generation(grid)

    flip()
    clock.tick(60)


pygame_quit()
quit()
