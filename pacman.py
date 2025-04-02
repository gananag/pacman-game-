import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initial grid setup
def initial_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    # Add walls
    for i in range(GRID_SIZE):
        grid[0][i] = 1  # Top wall
        grid[GRID_SIZE - 1][i] = 1  # Bottom wall
        grid[i][0] = 1  # Left wall
        grid[i][GRID_SIZE - 1] = 1  # Right wall
    # Add some inner walls
    for i in range(5, 15):
        grid[5][i] = 1
        grid[14][i] = 1
    # Add dots
    for i in range(1, GRID_SIZE - 1):
        for j in range(1, GRID_SIZE - 1):
            if grid[i][j] != 1:
                grid[i][j] = 2
    # Pacman starting position
    grid[10][10] = 3
    return grid

# Draw the grid
def draw_grid(screen, grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 1:  # Wall
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[y][x] == 2:  # Dot
                pygame.draw.circle(screen, YELLOW, rect.center, CELL_SIZE // 4)
            elif grid[y][x] == 3:  # Pacman
                pygame.draw.circle(screen, YELLOW, rect.center, CELL_SIZE // 2)

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman Game")
    clock = pygame.time.Clock()

    grid = initial_grid()
    pacman_position = (10, 10)
    score = 0
    direction = RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = UP
                elif event.key == pygame.K_DOWN:
                    direction = DOWN
                elif event.key == pygame.K_LEFT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    direction = RIGHT

        new_position = (pacman_position[0] + direction[0], pacman_position[1] + direction[1])
        if 0 <= new_position[0] < GRID_SIZE and 0 <= new_position[1] < GRID_SIZE and grid[new_position[1]][new_position[0]] != 1:
            grid[pacman_position[1]][pacman_position[0]] = 0
            pacman_position = new_position
            if grid[pacman_position[1]][pacman_position[0]] == 2:
                score += 1
            grid[pacman_position[1]][pacman_position[0]] = 3

        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()