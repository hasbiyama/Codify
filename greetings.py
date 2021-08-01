from srcode import *

class Name:

	def __init__(self, inp, arg): 

		self.inp = inp
		self.arg = arg

	def nameGreet(self):

		print("\n\t   *******************")
		print("\t>> Good " + self.arg  + ", " + colored(str(self.inp).upper(), 'magenta', attrs=['bold']) + "!")
		print("\t   *******************")

if __name__ == '__main__':
	fileFunc()