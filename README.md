# kitronik motor driver 5620 in python
A package in python, for the [Kitronik Motor Driver Board 5620](https://kitronik.co.uk/products/5620-motor-driver-board-for-the-bbc-microbit-v2) for the BBC micro:bit.

![logo](https://github.com/mimidbe/kitronik-motor-driver-5620-in-python/blob/main/images/circuit.png)    ![logo](https://github.com/mimidbe/kitronik-motor-driver-5620-in-python/blob/main/images/circuit1.jpg)


## Code Example
```Python
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
	
```

## Code Example
```Python
from microbit import *
from kitronik_motor_driver import *

sv1 = KServo(pin0)
while True:
    if button_a.is_pressed():
        sv1.writeAngle(50) # turn servo to 50 degrees 
    elif button_b.is_pressed():
        sv1.writeAngle(0) # return servo to 0 degrees         
```


## License
MIT

## Supported targets
for BBC micro:bit.
