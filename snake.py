import pygame
from pygame import KEYDOWN
from random import randrange

# --- SETTINGS ---
TILE_SIZE = 50  # Size of each square in pixels
GRID_WIDTH_X = 10
GRID_HEIGHT_Y = 10
WINDOW_WIDTH = TILE_SIZE * GRID_WIDTH_X
WINDOW_HEIGHT = TILE_SIZE * GRID_HEIGHT_Y

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)

# --- INIT PYGAME ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zmeika")

# Example: simple map data (0 = empty, 1 = wall)
game_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# --- MAIN LOOP ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw grid based on map
    for y in range(GRID_HEIGHT_Y):
        for x in range(GRID_WIDTH_X):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            if game_map[y][x] == 1:
                pygame.draw.rect(screen, BLUE, rect)  # Wall
            pygame.draw.rect(screen, BLACK, rect, 1)  # Grid outline

    pygame.display.flip()

    # Snake logic
    snake_live = True
    queue = []
    y_change, x_change = 0, 0
    y, x = 0, 1
    snake_length = 2
    food_rect = None
    snake_time = 350

    while snake_live:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake_live = False
                running = False
                break
            elif event.type == KEYDOWN and event.key == pygame.K_w:
                y_change, x_change = -1, 0
            elif event.type == KEYDOWN and event.key == pygame.K_a:
                y_change, x_change = 0, -1
            elif event.type == KEYDOWN and event.key == pygame.K_s:
                y_change, x_change = 1, 0
            elif event.type == KEYDOWN and event.key == pygame.K_d:
                y_change, x_change = 0, 1

        y, x = y_change + y, x_change + x







        if x > GRID_WIDTH_X:
            x = 0
        elif y > GRID_HEIGHT_Y:
            y = 0
        elif x < 0:
            x = GRID_WIDTH_X - 1
        elif y < 0:
            y = GRID_HEIGHT_Y - 1




        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

        if rect in queue:
            snake_live = False

        if food_rect == rect:
            snake_length += 1
            food_rect = None
            snake_time -= 10

        pygame.draw.rect(screen, (255, 15, 15), rect)
        queue.append(rect)

        if len(queue) > snake_length:
            pygame.draw.rect(screen, WHITE, queue[0])
            pygame.draw.rect(screen, BLACK, queue[0], 1)
            queue.pop(0)

        # adding food

        if food_rect is None:
            food_rect = pygame.Rect(randrange(GRID_WIDTH_X) * TILE_SIZE, randrange(GRID_HEIGHT_Y) * TILE_SIZE,
                                    TILE_SIZE, TILE_SIZE)
            while food_rect in queue:
                food_rect = pygame.Rect(randrange(GRID_WIDTH_X) * TILE_SIZE, randrange(GRID_HEIGHT_Y) * TILE_SIZE,
                                        TILE_SIZE, TILE_SIZE)
        else:
            pygame.draw.rect(screen, BLUE, food_rect)

        pygame.display.update()
        pygame.time.delay(snake_time)

pygame.quit()
