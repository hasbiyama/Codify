from srcode import *
from rmdir import *
from backcode import Attributes
from backcode import Input

ptoF1 = '../data'
os.chdir(ptoF1)

def codeGen():

	init()

	if inp == "":
		print(colored("\n\t[x] Please input your name!", 'red', attrs=['bold']))
		sys.exit()
	else: pass		

	Itter(cr_time).elseIf() # class

	Remdir(inp).remDir() # class

	inp2 = input("\n\t[?] Would you like me to generate your code? (y/n) : ")
	print("")

	if inp2.lower() == y:

		inp3 = input("\t[?] What do you want me to codify: ")
		print("")

		inp4 = input("\t[?] How long is your code length: ")	
		print("")

		result = "".join((random.choice(ltr + inp3)) for x in range(int(inp4)))

		print("\t   ++++++++++++++++")	
		print("\t>> Hey, yo!")
		print("\t   Here's your code:", colored(result, 'yellow', attrs=['bold']))
		print("\t   ++++++++++++++++\n")

		print("\t[!] have a nice day ~")
		
		time.sleep(1)

		isfileExist = Attributes(uD1, inp, 1, 2, 3, "Time: ", inp3=inp3, 
						 		length=inp4, code='Code: ', result=result)
		isfileExist.pherr()

	elif inp2.lower() == n :
		print("\t+++++++++++++++++++++++++") 
		print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
		print("\t+++++++++++++++++++++++++")

		time.sleep(1)

		isfileExist = Attributes(uD2, inp, 1, 2, 3, "Aborting at: ")
		isfileExist.pherr() 

	else : 
		print("\t++++++++++++++++++++++++++++++++++++++++")
		print(colored("\t[x] Try again, that's not a valid answer", 'red', attrs=['bold']))
		print("\t++++++++++++++++++++++++++++++++++++++++")

		time.sleep(1)
		isfileExist = Attributes(uD3, inp, 1, 2, 3, "Attempting at: ")
		isfileExist.pherr()		

if __name__ == '__main__':
	codeGen()