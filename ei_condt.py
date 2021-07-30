from fr_condt import *
from srcode import *

ptoF1 = '../data'
os.chdir(ptoF1)

class Option:

	def __init__(self, opt):

		self.opt = opt

	def optFunc(self):

		print("\n\t[?] Type a user or time (e.g. 'Albert' or 'Thu Jul 29'):\n")
		
		inpSp1 = input("\t>>  ")
		
		print("")

		if self.opt == a:
			ForL(inpSp1, file=uD0).frLoop()


		elif self.opt == b:
			ForL(inpSp1, file=uD1).frLoop()


		elif self.opt == c:
			ForL(inpSp1, file=uD3).frLoop()
	
		
		elif self.opt == d:
			ForL(inpSp1, file=uD2).frLoop()

