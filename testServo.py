from microbit import *
import kitronik_motor_driver

sv1 = KServo(pin0)
while True:
    if button_a.is_pressed():
        sv1.writeAngle(50) # turn servo to 50 degrees 
    elif button_b.is_pressed():
        sv1.writeAngle(0) # return servo to 0 degrees 
