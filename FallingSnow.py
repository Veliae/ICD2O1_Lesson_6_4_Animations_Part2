import pygame
import random

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
# Create an empty list
snow_list = []

# Create 50 random points
for i in range(50):
	# Create a random x and y coordinate between 0 and the width/height
    x = random.randrange(WIDTH + 1)
    y = random.randrange(HEIGHT + 1)

    # Add each point to the snow_list
    snow_list.append([x, y])

print(snow_list)

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
    # Update the location of each snowflake
    for item in snow_list:
      item[1] += 1
      if item[1] > HEIGHT:
         item[1] = 0
         item[0] = random.randrange(WIDTH + 1)

    # ----- DRAWING -----
    screen.fill(light_blue)  # always the first drawing command

    # Draw a snowflake at each random point from snow_list
    for item in snow_list:
       pygame.draw.circle(screen, white, item, 2)

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
