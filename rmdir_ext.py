import backcode
import condt
from srcode import *

class Remdirext:

	def __init__(self): pass

	def ifExt(self):

		srcf0 = os.listdir('../data')

		for x in srcf0: 

			if x.endswith('.txt'):

				conditional = condt.Conditional(inp)
				conditional.greetings()

			elif not x.endswith('.txt'):

				inpNew = input("\n\t[?] No database found!\n\t    What you gonna do: (a) Create | (b) Exit ->  ")

				if inpNew.lower() == a: pass		

				elif inpNew.lower() == b:

					print("")
					print("\t+++++++++++++++++++++++++") 
					print(colored("\t[!] Aborting ... bye!", 'green', attrs=['blink']))
					print("\t+++++++++++++++++++++++++")

					backcode.Attributes(uD2, inp, 1, 2, 3, "Aborting at: ").pherr()	
					time.sleep(1) 
					sys.exit()				

				elif inpNew.lower() == "":
					print(colored("\n\t[x] Please input your option!", 'red', attrs=['bold']))
					sys.exit()

				else: 
					print("\n\t++++++++++++++++++++++++++++++++++++")
					print(colored("\t[x] Try again, there's no {" + inpNew + "} option", 'red', attrs=['bold']))
					print("\t++++++++++++++++++++++++++++++++++++")
					
					time.sleep(1)
					sys.exit()

			else: pass
		
if __name__ == '__main__':
	ifExt()