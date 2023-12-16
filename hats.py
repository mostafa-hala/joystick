import pygame
import sys

pygame.init()

# Initialize the joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick found. Exiting.")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Check if the joystick has hats
if joystick.get_numhats() == 0:
    print("No hat found on the joystick. Exiting.")
    sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the hat position
    hat_position = joystick.get_hat(0)

    # Print the hat position
    print("Hat Position:", hat_position)

    # Delay to avoid printing too rapidly
    pygame.time.delay(100)
