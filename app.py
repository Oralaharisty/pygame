import pygame
import sys

# Pygame initialization
pygame.init()

# Defining constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CIRCLE_RADIUS = 30
FPS = 60

# Setting window sizes
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Circle")

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initial coordinates of the circle
circle_x, circle_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# Circle speed
speed = 5

# Create a timer to control the frame rate
clock = pygame.time.Clock()

# Main application loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Processing keys for control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= speed
    if keys[pygame.K_RIGHT]:
        circle_x += speed
    if keys[pygame.K_UP]:
        circle_y -= speed
    if keys[pygame.K_DOWN]:
        circle_y += speed

    # Limit the circle within the window
    circle_x = max(CIRCLE_RADIUS, min(circle_x, SCREEN_WIDTH - CIRCLE_RADIUS))
    circle_y = max(CIRCLE_RADIUS, min(circle_y, SCREEN_HEIGHT - CIRCLE_RADIUS))

    # Screen cleaning
    screen.fill(BLACK)

    # Draw a circle
    pygame.draw.circle(screen, WHITE, (circle_x, circle_y), CIRCLE_RADIUS)

    # Screen update
    pygame.display.flip()

    # Delay to control frame rate
    clock.tick(FPS)
