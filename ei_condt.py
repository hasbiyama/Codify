import fr_condt
from srcode import *

class Option:

	def __init__(self, opt):

		self.opt = opt

	def optFunc(self):

		print("\n\t[?] Type a user or time (e.g. 'Albert' or 'Thu Jul 29'):\n")
		
		inpSp1 = input("\t>>  ")
		
		print("")

		if inpSp1 == "" :
	
			print(colored("\t[x] This line cannot be empty!", 'red', attrs=['bold']))
	
			sys.exit()

		else: pass

		# searching input

		if self.opt == a:
			fr_condt.ForL(inpSp1, file=uD0).frLoop()


		elif self.opt == b:
			fr_condt.ForL(inpSp1, file=uD1).frLoop()


		elif self.opt == c:
			fr_condt.ForL(inpSp1, file=uD3).frLoop()
	
		
		elif self.opt == d:
			fr_condt.ForL(inpSp1, file=uD2).frLoop()

		elif self.opt == e:
			fr_condt.ForL(inpSp1, file=uD4).frLoop()

if __name__ == '__main__':
	optFunc()

