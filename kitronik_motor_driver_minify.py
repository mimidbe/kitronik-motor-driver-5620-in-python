G='motor 2'
F='motor 1'
from microbit import pin0 as A,pin8 as E,pin12 as B,pin16 as C
class KMotor:
	def __convert(self,x):return 1023*x//100
	def motorOn(self,H,dir,S):
		K='reverse';J='forward';D=self.__convert(S)
		if H==F:
			if dir==J:E.write_analog(D);B.write_digital(0)
			elif dir==K:B.write_analog(D);A.write_digital(0)
		elif H==G:
			if dir==J:A.write_analog(D);C.write_digital(0)
			elif dir==K:C.write_analog(D);A.write_digital(0)
	def motorOff(self,D):
		if D==F:E.write_digital(0);B.write_digital(0)
		elif D==G:A.write_digital(0);C.write_digital(0)
	def motorBrake(H,D):
		if D==F:E.write_digital(1);B.write_digital(1)
		elif D==G:A.write_digital(1);C.write_digital(1)
class KServo:
	def __init__(self,pin,freq=50,min_us=600,max_us=2400,angle=180):self.min_us=min_us;self.max_us=max_us;self.us=0;self.freq=freq;self.angle=angle;self.pin=pin;B=round(1/self.freq*1000);self.pin.set_analog_period(B)
	def __write_us(self,us):us=min(self.max_us,max(self.min_us,us));B=round(us*1024*self.freq//1000000);self.pin.write_analog(B);sleep(100);self.pin.write_digital(0)
	def writeAngle(self,degrees=None):B=degrees%360;C=self.max_us-self.min_us;D=self.min_us+C*B//self.angle;self.__write_us(D)
