import pygame
import sys
import time

pygame.init()

# Initialize the joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick found. Exiting.")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the positions of all axes
    axis_positions = [joystick.get_axis(1)]


    # Print the positions of all axes
    for i, position in enumerate(axis_positions):
        print(f"Axis {i} Position: {position}")
        time.sleep(0.1)

    # Delay to avoid printing too rapidly
    pygame.time.delay(100)
