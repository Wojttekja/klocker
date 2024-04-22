import pygame
from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
serwo = GPIO.PWM(17, 50)
serwo.start(7.5)

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
while loop:
    pygame.event.clear()
    if js.get_button(1) == 1:
        print("DOSC")
        serwo.stop()
        GPIO.cleanup()
        loop = False
    print(round(js.get_axis(0),1), (-(round(js.get_axis(0), 1))+1.5)/20)
    serwo.ChangeDutyCycle((-(round(js.get_axis(0), 1))+1.5)/20)
    sleep(0.01)