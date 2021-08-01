import admin_init
from srcode import *
import file_create_add
import ext_folder_create
import time_for_greetings

class Folder:

	def __init__(self): pass 
		
	def createFolder():


		if path.exists("../data"):

			os.chdir("../data")

			inp = input("\n\t[?] Hi! What's yourname? ->  ").lower()

			time_for_greetings.Time(inp, cr_time).printTime() # module

			file_create_add.Attributes(uD4, inp, 1, 2, 3, "Login at: ").createFile() 

			if inp == "":

				print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		
				sys.exit()
			
			else: pass

			with open('username.txt', 'r') as f:
					
				for ln in f:
					
					if inp in ln:

						ext_folder_create.Find().noFile()

					else: pass

				print(colored("\n\t[!] I'm sorry, you are not registered.", 'red', attrs=['bold']))

				print(colored("\t    * Please ask a member or admin to add you.", 'green', attrs=['bold']))

				time.sleep(1)

				sys.exit()

		
		elif not path.exists("../data"):

			admin_init.Guide().greets()

			inp = input("\n\t[?] What's yourname? ->  ").lower()

			if inp == "":

				print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		
				sys.exit()

			else : pass

			time_for_greetings.Time(inp, cr_time).printTime() # module

			admin_init.Guide(inp=inp).adminAdd()

			

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

			file_create_add.Attributes(uD4, inp, 1, 2, 3, "This file was created at : ").createFile() 

			# (uD0) USERNAME.TXT

			file_create_add.Attributes(uD0, inp, 1, 2, 3, "This file was created at : ").createFile()
			
			# (uD1) USERCODE.TXT

			isfileExist = file_create_add.Attributes(uD1, inp, 1, 2, 3, "This file was created at : ", code='admin')
			isfileExist.createFile()

			# (uD2) USERABORT.TXT

			file_create_add.Attributes(uD2, inp, 1, 2, 3, "This file was created at : ").createFile() 

			# (uD3) INVALID INPUT.TXT

			file_create_add.Attributes(uD3, inp, 1, 2, 3, "This file was created at : ").createFile()		

			# --------------------

			ext_folder_create.Find().noFile()
			

		else: pass


if __name__ == '__main__':
	remDir()