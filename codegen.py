import folder_create
import file_create_add
from srcode import *

def codeGen():

	folder_create.Folder.createFolder() # module

	os.chdir("../data") # new current dir

def inputPart():

	inp0 = input("\n\t[?] What's the username you wanna add? ->  ").lower()
	print("")

	with open(uD1, 'r') as f:
			
		for ln in f:
			
			if inp0 in ln:

				time.sleep(1)

				print(colored("\t[!] User '" + inp0 + "' already exists in " + uD1, 'yellow', attrs=['bold']))
				
				time.sleep(1)

				sys.exit()

			else: pass

	print(colored("\t[*] Adding " + inp0 + " to " + uD0 + "... ", 'cyan', attrs=['bold']))
	
	file_create_add.Attributes(uD0, inp0, 1, 2, 3, "Added at: ").createFile() 

	time.sleep(2)

	print("\t++++++++++++++++++++++++++++++++++++++++")
	print(colored("\t[+] User " + inp0 + " has been added!", 'green', attrs=['bold']))
	print("\t++++++++++++++++++++++++++++++++++++++++\n")

	inp2 = input("\t[?] Would you like me to generate the code? (y/n) : ")
	print("")

	if inp2.lower() == y:

		inp3 = input("\t[?] What do you want me to codify? -> ")
		print("")

		if inp3 == "":

			print(colored("\t[x] The input must not empty!", 'red', attrs=['bold']))
		
			sys.exit()                                

		else: pass

		inp4 = input("\t[?] How long is your code length? -> ")
		print("")

		if inp4 == "":

			print(colored("\t[x] Please input your code length!", 'red', attrs=['bold']))
		
			sys.exit()                                

		else: pass

		result = "".join((random.choice(ltr + inp3)) for x in range(int(inp4)))

		time.sleep(2)

		print("\t   ++++++++++++++++")	
		print("\t>> Hey, yo!")
		print("\t   Here's your code:", colored(result, 'yellow', attrs=['bold']))
		print("\t   ++++++++++++++++\n")
		
		time.sleep(1)
		
		print(colored("\t[!] have a nice day ~", 'green', attrs=['bold']))
		
		# USERCODE.TXT

		isfileExist = file_create_add.Attributes(uD1, inp0, 1, 2, 3, "Time: ", inp3=inp3, 
										length=inp4, code='Code: ', result=result)
		isfileExist.createFile()

		sys.exit()

	elif inp2.lower() == n :

		print("\n\t+++++++++++++++++++++++++") 
		print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
		print("\t+++++++++++++++++++++++++")

		file_create_add.Attributes(uD2, inp0, 1, 2, 3, "Aborting at: ").createFile() 

		time.sleep(1)

		sys.exit()

	else : 
		print("\t++++++++++++++++++++++++++++++++++++++++")
		print(colored("\t[x] Try again, that's not a valid answer", 'red', attrs=['bold']))
		print("\t++++++++++++++++++++++++++++++++++++++++")

		file_create_add.Attributes(uD3, inp0, 1, 2, 3, "Attempting at: ").createFile()		

		time.sleep(1)

		sys.exit()

if __name__ == '__main__':
	codeGen()