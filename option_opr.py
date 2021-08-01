import input_find
import input_remove
import codegen
import changecode
from srcode import *

class Exists:

	def __init__(self, arg=''):

		self.arg = arg

	def dataExists(self):
		
		print("\n\t[?] Database exists! What you gonna do?")
		inpGr = input("\n\t   (a) Remove | (b) Add \n\t   (c) Find   | (d) Change code | ->  ")

		if inpGr.lower() == a:

			print("\n\t[?] What do you want to remove? ")

			print(colored("\n\t[!] Never remove " + colored("'admin'", 'yellow') + colored(" on username", 'red'),'red', attrs=['bold']))
			
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

			input_remove.Remove(inpA).db_Remove()

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

			input_find.Search(inpSp).db_Search()

		elif inpGr.lower() == d: 

			changecode.reType()

		else: 

			print("\n\t++++++++++++++++++++++++++++++++++++")
			print(colored("\t[x] Try again, there's no {" + inpGr + "} option", 'red', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++")
			time.sleep(1)
			sys.exit()

if __name__ == '__main__':
	dataExists()

 

				




		







