import ei_condt
import rm_condt
import codegen
import changecode
from srcode import *

class Conditional:

	def __init__(self, arg=''):

		self.arg = arg

	def greetings(self):
		
		print("\n\t[?] Database exists! What you gonna do?")
		inpGr = input("\n\t   (a) Remove | (b) Add \n\t   (c) Find   | (d) Change code | ->  ")

		if inpGr.lower() == a:

			print("\n\t[?] What do you want to remove? ")
			
			inpA = input("\n\t   (a) username  | (b) usercode \n\t   (c) userabort | (d) invalid_input \n\t   (e) login_rec |  -> ")

			if inpA.lower() == a: pass 
			elif inpA.lower() == b: pass
			elif inpA.lower() == c: pass 
			elif inpA.lower() == d: pass
			elif inpA.lower() == e: pass

			else:
				print("\n\t++++++++++++++++++++++++++++++++++++")
				print(colored("\t[x] Try again, there's no {" + inpA + "} option", 'red', attrs=['bold']))
				print("\t++++++++++++++++++++++++++++++++++++")
				
				time.sleep(1)
				sys.exit()

			rm_condt.Rmoption(inpA).optFunc()

			print(colored("\t[!] Done!", 'green', attrs=['bold']))
			sys.exit()
			
		elif inpGr.lower() == b: 

			codegen.inputPart()

		elif inpGr.lower() == c: 
			
			print("\n\t[?] What do you want to find? ")
			inpSp = input("\n\t   (a) username  | (b) usercode \n\t   (c) userabort | (d) invalid_input \n\t   (e) login_rec |  -> ")

			if inpSp.lower() == a: pass 
			elif inpSp.lower() == b: pass
			elif inpSp.lower() == c: pass 
			elif inpSp.lower() == d: pass
			elif inpSp.lower() == e: pass

			else:
				print("\n\t++++++++++++++++++++++++++++++++++++")
				print(colored("\t[x] Try again, there's no {" + inpSp + "} option", 'red', attrs=['bold']))
				print("\t++++++++++++++++++++++++++++++++++++")
				
				time.sleep(1)
				sys.exit()

			ei_condt.Option(inpSp).optFunc()

		elif inpGr.lower() == d: 

			changecode.retype()

		else: 

			print("\n\t++++++++++++++++++++++++++++++++++++")
			print(colored("\t[x] Try again, there's no {" + inpGr + "} option", 'red', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++")
			time.sleep(1)
			sys.exit()

if __name__ == '__main__':
	greetings()

 

				




		







