from microbit import *

'''
 * Blocks for driving the Kitronik Motor Driver Board
'''
''' weight=100 color=#00A654 icon="\uf21c" block="Motor Driver" '''
class kitronik_motor_driver: 
	'''************************************************************************************************************************************************
	* micro:bit motor driver blocks 
	************************************************************************************************************************************************'''
    '''Note that Forward and reverse are slightly arbitrary, as it depends on how the motor is wired...'''

	'''**
     * Turns on motor specified by eMotors in the direction specified
     * by eDirection, at the requested speed 
     *
	 * @param motor which motor to turn on
	 * @param dir   which direction to go
	 * @param speed how fast to spin the motor
     *'''
    ''' blockId=kitronik_motordriver_motor_on
      block="%motor|on direction %dir|speed %speed"
      speed.min=0 speed.max=100 '''
    def _convert(self, x, i_m, i_M):
        return max(min(1023, (x - i_m) * 1023 // (i_M - i_m)), 0)
        
    def motorOn(self, motor, dir, speed): 
        # first convert 0-100 to 0-1024 (approx) 
        OutputVal = self._convert(speed, 0, 100) * 10

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
	'''
     * Turns off the motor specified by eMotors
     * @param motor :which motor to turn off
     '''
    ''' blockId=kitronik_motordriver_motor_off
     block="turn off %motor" '''
    def motorOff(self, motor):
        if motor == "motor 1": 
                pin8.write_digital(0)
                pin12.write_digital(0)
        elif motor == "motor 2":
                pin0.write_digital(0)
                pin16.write_digital(0)
    def motor_brake(self,motor):
	if motor==KMotor.MOTOR_1:
		pin8.write_digital(1)
		pin12.write_digital(1)
        elif motor == "motor 2":
		pin0.write_digital(1)
		pin16.write_digital(1)

