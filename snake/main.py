import random
import pygame as pyg

TILE_SIZE = 25
SCREEN_SIZE = TILE_SIZE * TILE_SIZE

GREEN = (20, 84, 33)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class Food:

    def __init__(self):
        self.pos = self.random_pos()

    def random_pos(self):
        width = random.randrange(0, SCREEN_SIZE, 25)
        height = random.randrange(0, SCREEN_SIZE, 25)

        return pyg.Rect(width, height, TILE_SIZE, TILE_SIZE)


class Snake:

    def __init__(self):
        self.pos = pyg.Rect(SCREEN_SIZE / 2, SCREEN_SIZE / 2, TILE_SIZE, TILE_SIZE)

    def snake_movement(self):
        keys = pyg.key.get_pressed()
        print(self.pos)

        if keys[pyg.K_w]:
            self.pos.y -= TILE_SIZE
        if keys[pyg.K_s]:
            self.pos.y += TILE_SIZE
        if keys[pyg.K_a]:
            self.pos.x -= TILE_SIZE
        if keys[pyg.K_d]:
            self.pos.x += TILE_SIZE


pyg.init()
screen = pyg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pyg.time.Clock()
running = True


food = Food()
snake = Snake()

while running:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill(BLACK)

    pyg.draw.rect(screen, GREEN, snake.pos)
    pyg.draw.rect(screen, RED, food.pos)

    snake.movement()

    pyg.display.flip()
    clock.tick(60)

pyg.quit()
