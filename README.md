# kitronik-motor-driver-5620-in-python
A package in python, for the [Kitronik Motor Driver Board 5620](https://kitronik.co.uk/products/5620-motor-driver-board-for-the-bbc-microbit-v2) for the BBC micro:bit.


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
        theBoard.motorOff("motor 1")
```

## License
MIT

## Supported targets
for BBC micro:bit (The metadata above is needed for package search.
