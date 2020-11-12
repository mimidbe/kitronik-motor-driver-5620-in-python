from microbit import pin0,pin8,pin12,pin16

class KMotor: 
  '''*************************
     * motor driver  
     *************************
    Note that Forward and reverse are slightly arbitrary, 
    as it depends on how the motor is wired...
    Turns on motor specified by eMotors in the direction specified
    by eDirection, at the requested speed 
    Args:
       * motor which motor to turn on
       * dir   which direction to go
       * speed how fast to spin the motor
    Usage:
      Mot1 = Kmotor()
      Mot1.motorOn("motor 1", "forward", 10) 
       ''' 

    # convert 0-100 to 0-1024 (approx) 
    def __convert(self, x):
        return int((1023/100)*x)
        
    def motorOn(self, motor, dir, speed): 
        # first convert 0-100 to 0-1024 (approx) 
        OutputVal = self.__convert(speed)

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
		
class KServo:
    """***********************
     * servo driver  
     *************************
    Args:
        * pin (pin0,pin16,pin8,pin12): The pin where servo is connected.
        * freq (int): The frequency of the signal, in hertz.
        * min_us (int): The minimum signal length supported by the servo.
        * max_us (int): The maximum signal length supported by the servo.
        * angle (int): The angle between minimum and maximum positions.
    Usage:
        SG90 @ 3.3v servo connected to pin0
	sv1 = KServo(pin0)
        sv1.write_angle(50) # turn servo to 50 degrees 
    """

    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def __write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        self.pin.write_digital(0)  # turn the pin off

    def writeAngle(self, degrees=None):
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.__write_us(us)

