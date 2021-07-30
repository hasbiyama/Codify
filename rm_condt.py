from fr_condt import *
from rm_fr_condt import *
from srcode import *

ptoF1 = '../data'
os.chdir(ptoF1)

class Rmoption:

	def __init__(self, opt):

		self.opt = opt

	def optFunc(self):

		print("\n\t[?] Type a user and/or time (e.g. 'Albert' or 'Thu Jul 29'):\n")
		
		inpSp1 = input("\t>>  ")
		
		print("")


		if self.opt == a:
			Rmforl(inpSp1, file=uD0).frLoop()


		elif self.opt == b:
			Rmforl(inpSp1, file=uD1).frLoop()


		elif self.opt == c:
			Rmforl(inpSp1, file=uD2).frLoop()
	
		
		elif self.opt == d:
			Rmforl(inpSp1, file=uD3).frLoop()
