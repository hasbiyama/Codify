import greetings
from srcode import *

class Time:

	def __init__(self, inp, cr_time): 

		self.cr_time = cr_time
		self.inp = inp

	def printTime(self):

		if self.cr_time in range(3, 11): 
			greetings.Name(self.inp, DN_TIME[0]).nameGreet()

		elif self.cr_time in range(11, 14): 
			greetings.Name(self.inp, DN_TIME[1]).nameGreet()

		elif self.cr_time in range(14, 19): 
			greetings.Name(self.inp, DN_TIME[2]).nameGreet()

		elif self.cr_time in range(19, 24): 
			greetings.Name(self.inp, DN_TIME[3]).nameGreet()

		elif self.cr_time in range(0, 3):
			greetings.Name(self.inp, DN_TIME[3]).nameGreet()
		else:
			pass

if __name__ == '__main__':
	printTime()