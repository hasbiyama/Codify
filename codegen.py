import rmdir
import itrcls
import backcode
import rmdir_ext
from srcode import *

def codeGen():

	init()

	if inp == "":
		print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		sys.exit()
	else: pass
	
	itrcls.Itter(cr_time).elseIf() # module

	rmdir.Remdir(inp).remDir() # module

	os.chdir("../data") # new current dir

def inputPart():

	inp2 = input("\n\t[?] Would you like me to generate your code? (y/n) : ")
	print("")

	if inp2.lower() == y:

		inp3 = input("\t[?] What do you want me to codify: ")
		print("")

		inp4 = input("\t[?] How long is your code length: ")
		print("")

		result = "".join((random.choice(ltr + inp3)) for x in range(int(inp4)))

		if inp4 == "":

			print(colored("\t[x] This line cannot be empty!", 'red', attrs=['bold']))
		
			sys.exit()                                

		else: pass

		print("\t   ++++++++++++++++")	
		print("\t>> Hey, yo!")
		print("\t   Here's your code:", colored(result, 'yellow', attrs=['bold']))
		print("\t   ++++++++++++++++\n")

		print(colored("\t[!] have a nice day ~", 'green', attrs=['bold']))
		
		# USERCODE.TXT

		isfileExist = backcode.Attributes(uD1, inp, 1, 2, 3, "Time: ", inp3=inp3, 
										length=inp4, code='Code: ', result=result)
		isfileExist.pherr()

		time.sleep(1)

		sys.exit()

	elif inp2.lower() == n :
		print("\t+++++++++++++++++++++++++") 
		print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
		print("\t+++++++++++++++++++++++++")

		time.sleep(1)

	else : 
		print("\t++++++++++++++++++++++++++++++++++++++++")
		print(colored("\t[x] Try again, that's not a valid answer", 'red', attrs=['bold']))
		print("\t++++++++++++++++++++++++++++++++++++++++")

		time.sleep(1)

if __name__ == '__main__':
	codeGen()