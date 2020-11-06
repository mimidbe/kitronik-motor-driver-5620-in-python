# kitronik motor driver 5620 in python
A package in python, for the [Kitronik Motor Driver Board 5620](https://kitronik.co.uk/products/5620-motor-driver-board-for-the-bbc-microbit-v2) for the BBC micro:bit.

![logo](https://github.com/mimidbe/kitronik-motor-driver-5620-in-python/blob/main/images/circuit.png){:height="50%" width="50%"}  ![logo](https://github.com/mimidbe/kitronik-motor-driver-5620-in-python/blob/main/images/circuit1.jpg)


## Code Example
```Python
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
	theBoard.motorOn("motor 1", "forward", 50)
        theBoard.motorOn("motor 2", "forward", 50)
```

## License
MIT

## Supported targets
for BBC micro:bit.
