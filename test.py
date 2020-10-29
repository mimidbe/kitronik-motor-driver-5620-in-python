from microbit import *
import kitronik_motor_driver


while True:
    theBoard = kitronik_motor_driver
    if button_a.is_pressed():
        theBoard.motorOn("motor 1", "forward", 10)
        theBoard.motorOn("motor 2", "reverse", 100)
    if button_b.is_pressed():
        theBoard.motorOff("motor 1")
        theBoard.motorOff("motor 2")
    else:
	theBoard.motorOff("motor 1", "forward", 50)
        theBoard.motorOff("motor 2", "forward", 50)

        
