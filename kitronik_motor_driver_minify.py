_D='reverse'
_C='forward'
_B='motor 2'
_A='motor 1'
from microbit import *
class KMotor:
	def __convert(self,x):return 1023*x//100
	def motorOn(self,motor,dir,speed):
		OutputVal=self.__convert(speed)
		if motor==_A:
			if dir==_C:pin8.write_analog(OutputVal);pin12.write_digital(0)
			elif dir==_D:pin12.write_analog(OutputVal);pin0.write_digital(0)
		elif motor==_B:
			if dir==_C:pin0.write_analog(OutputVal);pin16.write_digital(0)
			elif dir==_D:pin16.write_analog(OutputVal);pin0.write_digital(0)
	def motorOff(self,motor):
		if motor==_A:pin8.write_digital(0);pin12.write_digital(0)
		elif motor==_B:pin0.write_digital(0);pin16.write_digital(0)
	def motorBrake(self,motor):
		if motor==_A:pin8.write_digital(1);pin12.write_digital(1)
		elif motor==_B:pin0.write_digital(1);pin16.write_digital(1)
class KServo:
	def __init__(self,pin,freq=50,min_us=600,max_us=2400,angle=180):self.min_us=min_us;self.max_us=max_us;self.us=0;self.freq=freq;self.angle=angle;self.analog_period=0;self.pin=pin;analog_period=round(1/self.freq*1000);self.pin.set_analog_period(analog_period)
	def __write_us(self,us):us=min(self.max_us,max(self.min_us,us));duty=round(us*1024*self.freq//1000000);self.pin.write_analog(duty);sleep(100);self.pin.write_digital(0)
	def writeAngle(self,degrees=None):degrees=degrees%360;total_range=self.max_us-self.min_us;us=self.min_us+total_range*degrees//self.angle;self.__write_us(us)
