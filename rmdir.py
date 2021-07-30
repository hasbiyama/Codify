import sys
import codegen
from srcode import *
from condt import *
from backcode import *
from itrcls import *


class Remdir(Conditional):

	def __init__(self, inp, arg=''): 
		
		super().__init__(inp, arg)
		
	def remDir(self):

		if path.exists("../data"):
				
			if path.isfile('../data/username.txt'):

				condt = Conditional(inp)
				condt.greetings()

			elif not path.isfile('../data/username.txt'):

				inpNew = input("\n\t[?] No database found!\n\t    What you gonna do: (a) Create | (b) Exit ->  ")
				print("")

				if inpNew == a: 
					isfileExist = Attributes(uD0, inp, 1, 2, 3, "Login at: ")
					isfileExist.pherr()

				elif inpNew == b:

					print("\t+++++++++++++++++++++++++") 
					print(colored("\t[!] Aborting ... bye!", 'green', attrs=['blink']))
					print("\t+++++++++++++++++++++++++")

					isfileExist = Attributes(uD2, self.inp, 1, 2, 3, "Aborting at: ")
					isfileExist.pherr()	
					time.sleep(1) 
					sys.exit()				

				else: pass
			else: pass
		else: pass
