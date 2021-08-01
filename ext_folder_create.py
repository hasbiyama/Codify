import option_opr
from srcode import *
import file_create_add

class Find:

	def __init__(self): pass

	def noFile(self):

		srcf0 = os.listdir('../data')

		for x in srcf0: 

			if x.endswith('.txt'):

				options = option_opr.Exists()
				options.dataExists()

			elif not x.endswith('.txt'):

				inpNew = input("\n\t[?] No database found!\n\t    What you gonna do: (a) Create | (b) Exit ->  ")

				if inpNew.lower() == a: pass		

				elif inpNew.lower() == b:

					print("")
					print("\t+++++++++++++++++++++++++") 
					print(colored("\t[!] Aborting ... bye!", 'green', attrs=['blink']))
					print("\t+++++++++++++++++++++++++")

					file_create_add.Attributes(uD2, inp, 1, 2, 3, "Aborting at: ").createFile()	
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
	noFile()

