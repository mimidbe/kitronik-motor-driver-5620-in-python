from microbit import *
from kitronik_motor_driver import *

theBoard = KMotor()
while True:
    if button_a.is_pressed():
        theBoard.motorOn("motor 1", "forward", 10)
        theBoard.motorOn("motor 2", "reverse", 100)
    elif button_b.is_pressed():
        theBoard.motorOff("motor 1")
        theBoard.motorOff("motor 2")
    else:
	theBoard.motorOn("motor 1", "forward", 50)
        theBoard.motorOn("motor 2", "forward", 50)

        
