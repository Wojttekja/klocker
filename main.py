from gpiozero import Servo
import RPi.GPIO as GPIO
from time import sleep
from pygame import joystick, init, event

GPIO.setwarnings(False)

servoR = Servo(13, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, frame_width=20/1000)
servoL = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, frame_width=20/1000)

threshold = 0.05 #kat martwy

init()

while True:
    if joystick.get_count() > 0:
        break
    print("No controller detected")
    sleep(0.5)

print(f"Found {joystick.get_count()} joystick")
js = joystick.Joystick(0)
name = js.get_name()
js.init()
print(f"connected to {name}")

def servo_drive(x_axis, y_axis, mul):

    R_value = confined if abs( (confined := y_axis + x_axis) ) < 1 else (2*int(confined > 0) -1)
    L_value = confined if abs( (confined := -y_axis + x_axis) ) < 1 else (2*int(confined > 0) -1)
    #L_value = -y_axis - x_axis


    return R_value * mul, L_value * mul

while True:
    event.clear()
    x_axisL = confined if abs( (confined := round(js.get_axis(0), 2)) ) > threshold else 0
    y_axisL = confined if abs( (confined := round(js.get_axis(1), 2)) ) > threshold else 0

    x_axisR = confined if abs( (confined := round(js.get_axis(2), 2)) ) > threshold else 0
    y_axisR = confined if abs( (confined := round(js.get_axis(3), 2)) ) > threshold else 0

    print(f"{x_axisL} \t {y_axisL} \t {x_axisR} \t {y_axisR}", end="\r")

    servoR.value, servoL.value = servo_drive(x_axisL, y_axisL, 1)