import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Falling Snow")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (137, 207, 240)

# ---------------------------

# ---------------------------
# Functions


# ---------------------------

# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here


    # ----- DRAWING -----
    screen.fill(light_blue)  # always the first drawing command

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
