import ei_condt
import rm_condt
import codegen
from srcode import *

class Conditional:

	def __init__(self, inp, arg=''):

		self.arg = arg
		self.inp = inp

	def greetings(self):
		
		print("\n\t[?] Database exists! What you gonna do?")
		inpGr = input("\t   (a) Remove | (b) Add | (c) Find : ->  ")

		if inpGr.lower() == a:

			print("\n\t[?] What do you want to remove? ")
			inpA = input("\t   (a) username | (b) usercode | (c) userabort | (d) invalid_input ->  ")

			if inpA.lower() == a: pass 
			elif inpA.lower() == b: pass
			elif inpA.lower() == c: pass 
			elif inpA.lower() == d: pass

			else:
				print("\n\t++++++++++++++++++++++++++++++++++++")
				print(colored("\t[x] Try again, there's no {" + inpA + "} option", 'red', attrs=['bold']))
				print("\t++++++++++++++++++++++++++++++++++++")
				
				time.sleep(1)
				sys.exit()

			rm_condt.Rmoption(inpA).optFunc()

			print(colored("\t[!] Done!", 'green', attrs=['bold']))
			sys.exit()
			
		elif inpGr.lower() == b: codegen.inputPart()

		elif inpGr.lower() == c: 
			
			print("\n\t[?] What do you want to find? ")
			inpSp = input("\t   (a) users | (b) codes | (c) invalid login | (d) abort opr ->  ")

			if inpSp.lower() == a: pass 
			elif inpSp.lower() == b: pass
			elif inpSp.lower() == c: pass 
			elif inpSp.lower() == d: pass

			else:
				print("\n\t++++++++++++++++++++++++++++++++++++")
				print(colored("\t[x] Try again, there's no {" + inpSp + "} option", 'red', attrs=['bold']))
				print("\t++++++++++++++++++++++++++++++++++++")
				
				time.sleep(1)
				sys.exit()

			ei_condt.Option(inpSp).optFunc()

		else: 

			print("\n\t++++++++++++++++++++++++++++++++++++")
			print(colored("\t[x] Try again, there's no {" + inpGr + "} option", 'red', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++")
			time.sleep(1)
			sys.exit()

if __name__ == '__main__':
	greetings()

 

				




		







