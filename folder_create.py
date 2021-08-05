import admin_init
import verify_code
import option_opr
from srcode import *
import file_create_add
import time_for_greetings

class Folder:

	def __init__(self): pass 
		
	def createFolder():


		if path.exists("../data"):

			os.chdir("../data")

			inp = input("\n\t[?] Hi! What's yourname? ->  ").lower()

			file_create_add.Attributes(uD4, "Login at: ", 1, 2, 3, inp).createFile() 

			if inp == "":

				print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		
				sys.exit()
			
			elif re.findall(r'\d', inp):

				print(colored("\n\t[x] Name can only accept string!", 'red', attrs=['bold']))

				sys.exit()

			else: pass


			time_for_greetings.Time(inp, cr_time).printTime() # module

		
			with open(uD0) as f:

				fp = str(f.readlines())

				newF = fp.strip()

				for line in newF:
					
					if re.search(r"\buser: {}\b".format(inp), newF):

						verify_code.Verify(inp).verifyCode()

					else: 

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

			file_create_add.Attributes(uD4, "This file was created at : ", 1, 2, 3, inp).createFile() 

			# (uD0) USERNAME.TXT

			file_create_add.Attributes(uD0, "This file was created at : ", 1, 2, 3, inp).createFile()
			
			# (uD1) USERCODE.TXT

			isfileExist = file_create_add.Attributes(uD1, "This file was created at : ", 1, 2, 3, inp + ' Code: admin' + ' id: {}'.format('1'))
			isfileExist.createFile()

			# (uD2) USERABORT.TXT

			file_create_add.Attributes(uD2, "This file was created at : ", 1, 2, 3, inp).createFile() 

			# (uD3) INVALID INPUT.TXT

			file_create_add.Attributes(uD3, "This file was created at : ", 1, 2, 3, inp).createFile()		

			# --------------------

			option_opr.Exists().dataExists()
			

		else: pass


if __name__ == '__main__':
	createFolder()