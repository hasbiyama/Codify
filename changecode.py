import file_create_add
import remove_db
from srcode import *

def reType():


# RETYPING CODE


	inp0 = input("\n\t[*] Please re-type your name -> ")
	print("")

	x = "<user: " + inp0

	with open(uD1, 'r') as f:

		fp = f.readlines()

		for lsl in fp: 

			if inp0 in lsl:

				time.sleep(1)

				remove_db.File(inp0, file=uD1).removeFromFile()

				time.sleep(1)

			else: 

				time.sleep(2)

				print(colored("\t[!] Please type your name correctly", 'red', attrs=['bold']))
				time.sleep(1)
				sys.exit()


# REGENERATING CODE


	inp2 = input("\t[?] Would you like me to regenerate the code? (y/n) : ")
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

		print(colored("\t[*] Generating ...", 'cyan', attrs=['bold']))
		print("")

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

		time.sleep(1)

		sys.exit()

	else:

		print("\t++++++++++++++++++++++++++++++++++++++++")
		print(colored("\t[x] Try again, that's not a valid answer", 'red', attrs=['bold']))
		print("\t++++++++++++++++++++++++++++++++++++++++")

		file_create_add.Attributes(uD3, inp0, 1, 2, 3, "Attempting at: ").createFile()		

		time.sleep(1)

		sys.exit()

if __name__ == '__main__':
	reType()