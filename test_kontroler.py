import pygame
from time import sleep

pygame.init()

while True:
    if pygame.joystick.get_count() > 0:
        break   
    print("No controller detected")
    sleep(0.5)

print(f"Found {pygame.joystick.get_count()} joystick")
js = pygame.joystick.Joystick(0)
name = js.get_name()
js.init()
print(f"connected to {name}")

loop = True
while loop: # pętla
    pygame.event.clear()
    print(f"x: {round(js.get_axis(0),1)}, y: {round(js.get_axis(1),1)}", end="")
    print("\r", end="")
    if js.get_button(1) == 1:
        print('STOP')
        loop = False