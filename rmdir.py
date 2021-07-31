import itrcls
import rmdir_ext
import backcode
import admin_init
from srcode import *

class Remdir:

	def __init__(self): pass 
		
	def remDir():


		if path.exists("../data"):

			os.chdir("../data")

			inp = input("\n\t[?] Hi! What's yourname? ->  ").lower()

			itrcls.Itter(inp, cr_time).elseIf() # module

			backcode.Attributes(uD4, inp, 1, 2, 3, "Login at: ").pherr() 

			if inp == "":

				print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		
				sys.exit()
			
			else: pass

			with open('username.txt', 'r') as f:
					
				for ln in f:
					
					if inp in ln:

						rmdir_ext.Remdirext().ifExt()

					else: pass

				print(colored("\n\t[!] I'm sorry, you are not registered.", 'red', attrs=['bold']))

				print(colored("\t    * Please ask a member or admin to add you.", 'green', attrs=['bold']))

				time.sleep(1)

				sys.exit()

		
		elif not path.exists("../data"):

			admin_init.Initialiser().greets()

			inp = input("\n\t[?] What's yourname? ->  ").lower()

			itrcls.Itter(inp, cr_time).elseIf() # module

			if inp == "":

				print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		
				sys.exit()

			else : pass

			admin_init.Initialiser(inp=inp).adminAdd()

			

			# - > FOLDER CREATION

			

			print(colored("\n\t[!] Data folder doesn't exist.", 'red', attrs=['bold']))

			time.sleep(2)
			
			print(colored("\n\t[*] Creating ./data ... ", 'green', attrs=['bold']))
			
			time.sleep(2)
			
			os.makedirs("../data")

			print(colored("\n\t[+] ./data created!\n", 'yellow', attrs=['bold']))

			os.chdir("../data")

			

			# - > FILE CREATION

			
			# (uD4) LOGIN_REC.TXT

			backcode.Attributes(uD4, inp, 1, 2, 3, "Login at: ").pherr() 

			# (uD0) USERNAME.TXT

			backcode.Attributes(uD0, inp, 1, 2, 3, "Added at: ").pherr()
			
			# (uD1) USERCODE.TXT

			isfileExist = backcode.Attributes(uD1, inp, 1, 2, 3, "Time: ", code='Code: ')
			isfileExist.pherr()

			# (uD2) USERABORT.TXT

			backcode.Attributes(uD2, inp, 1, 2, 3, "Aborting at: ").pherr() 

			# (uD3) INVALID INPUT.TXT

			backcode.Attributes(uD3, inp, 1, 2, 3, "Attempting at: ").pherr()		

			# --------------------

			rmdir_ext.Remdirext().ifExt()
			

		else: pass


if __name__ == '__main__':
	remDir()