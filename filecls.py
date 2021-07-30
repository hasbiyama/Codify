from srcode import *

class Func:

	def __init__(self, inp, arg): 

		self.inp = inp
		self.arg = arg

	def fileFunc(self):

		print("\n\t   *******************")
		print("\t>> Good " + self.arg  + ", " + colored(str(self.inp).upper(), 'magenta', attrs=['bold']) + "!")
		print("\t   *******************")