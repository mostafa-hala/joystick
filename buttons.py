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

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check the state of multiple buttons
    button_states = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

    # Print the states of all buttons
    print("Button States:", button_states)

    # Delay to avoid printing too rapidly
    pygame.time.delay(100)
