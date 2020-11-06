from microbit import pin0,pin8,pin12,pin16

class kitronik_motor_driver: 
  '''*************************************************************************************************
     * micro:bit motor driver blocks 
     *************************************************************************************************
    Note that Forward and reverse are slightly arbitrary, as it depends on how the motor is wired...
     * Turns on motor specified by eMotors in the direction specified
     * by eDirection, at the requested speed 
     * @param motor which motor to turn on
     * @param dir   which direction to go
     * @param speed how fast to spin the motor''' 

    # convert 0-100 to 0-1024 (approx) 
    def _convert(self, x):
        return (1023/100)*x
        
    def motorOn(self, motor, dir, speed): 
        # first convert 0-100 to 0-1024 (approx) 
        OutputVal = self._convert(speed)

        if motor == "motor 1":  # Motor 1 uses Pins 8 and 12
            if dir == "forward":
                pin8.write_analog(OutputVal)
                # Write the low side digitally, 
                # to allow the 3rd PWM to be used if required elsewhere
                pin12.write_digital(0)  
            elif dir == "reverse":
                pin12.write_analog(OutputVal)
                pin0.write_digital(0)

        elif motor == "motor 2":  # Motor 2 uses Pins 0 and 16        
            if dir == "forward":
                pin0.write_analog(OutputVal)
                pin16.write_digital(0)
            elif dir == "reverse":
                pin16.write_analog(OutputVal)
                pin0.write_digital(0)
		
    def motorOff(self, motor):
        if motor == "motor 1": 
                pin8.write_digital(0)
                pin12.write_digital(0)
        elif motor == "motor 2":
                pin0.write_digital(0)
                pin16.write_digital(0)
		
    def motorBrake(self, motor):
	if motor == "motor 1":
		pin8.write_digital(1)
		pin12.write_digital(1)
        elif motor == "motor 2":
		pin0.write_digital(1)
		pin16.write_digital(1)

