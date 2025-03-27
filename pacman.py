import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
PACMAN_SIZE = 50
PACMAN_SPEED = 5
GHOST_SIZE = 50
GHOST_SPEED = 3
PELLET_SIZE = 10

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Set up the display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
FONT = pygame.font.Font(None, 36)

# Set up the clock
CLOCK = pygame.time.Clock()

# Set up the Pacman
PACMAN = pygame.Rect(WIDTH / 2, HEIGHT / 2, PACMAN_SIZE, PACMAN_SIZE)

# Set up the ghosts
GHOSTS = [
    pygame.Rect(100, 100, GHOST_SIZE, GHOST_SIZE),
    pygame.Rect(300, 300, GHOST_SIZE, GHOST_SIZE),
    pygame.Rect(500, 500, GHOST_SIZE, GHOST_SIZE),
]

# Set up the pellets
PELLETS = []
for _ in range(100):
    PELLETS.append(pygame.Rect(random.randint(0, WIDTH - PELLET_SIZE), random.randint(0, HEIGHT - PELLET_SIZE), PELLET_SIZE, PELLET_SIZE))

# Set up the score
SCORE = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Move the Pacman
    if keys[pygame.K_UP]:
        PACMAN.y -= PACMAN_SPEED
    if keys[pygame.K_DOWN]:
        PACMAN.y += PACMAN_SPEED
    if keys[pygame.K_LEFT]:
        PACMAN.x -= PACMAN_SPEED
    if keys[pygame.K_RIGHT]:
        PACMAN.x += PACMAN_SPEED

    # Keep the Pacman inside the screen
    if PACMAN.x < 0:
        PACMAN.x = 0
    if PACMAN.x > WIDTH - PACMAN_SIZE:
        PACMAN.x = WIDTH - PACMAN_SIZE
    if PACMAN.y < 0:
        PACMAN.y = 0
    if PACMAN.y > HEIGHT - PACMAN_SIZE:
        PACMAN.y = HEIGHT - PACMAN_SIZE

    # Move the ghosts
    for ghost in GHOSTS:
        if ghost.x < PACMAN.x:
            ghost.x += GHOST_SPEED
        if ghost.x > PACMAN.x:
            ghost.x -= GHOST_SPEED
        if ghost.y < PACMAN.y:
            ghost.y += GHOST_SPEED
        if ghost.y > PACMAN.y:
            ghost.y -= GHOST_SPEED

    # Check for collisions with the ghosts
    for ghost in GHOSTS:
        if PACMAN.colliderect(ghost):
            print("Game Over")
            pygame.quit()
            sys.exit()

    # Check for collisions with the pellets
    for pellet in PELLETS[:]:
        if PACMAN.colliderect(pellet):
            PELLETS.remove(pellet)
            SCORE += 1

    # Draw everything
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, YELLOW, PACMAN)
    for ghost in GHOSTS:
        pygame.draw.rect(SCREEN, RED, ghost)
    for pellet in PELLETS:
        pygame.draw.rect(SCREEN, WHITE, pellet)
    text = FONT.render(f"Score: {SCORE}", True, WHITE)
    SCREEN.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    CLOCK.tick(60)