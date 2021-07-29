from srcode import *
from backcode import Attributes
from backcode import Input
from oth_cond import *
from rmdir import *

ptoF1 = '../data'
os.chdir(ptoF1)

def codeGen():

	init()

	inp = input("\n\t>> Hi, what's yourname: ")

	print("\t   ***************************")
	print("\t>> Hello, " +  colored(str(inp).upper(), 'magenta', attrs=['bold']) + "!")
	print("\t   ***************************")

	# greets = Conditional(inp)

	isfileExist = Attributes(uD0, inp, 1, 2, 3, "Login at: ")
	isfileExist.pherr()

	inp2 = input("\n\t>> Would you like me to generate your code? (y/n) : ")

	if inp2 == y.lower():

		print("\t   =======================================")	
		inp3 = input("\t>> What do you want me to codify: ")
		print("\t   =============================")	
		inp4 = input("\t>> How long is your desired code: ")
		print("\t   =============================")	

		result = "".join((random.choice(ltr + inp3)) for x in range(int(inp4)))

		print("\t   +++++++++++++++++++++++++++++++++++++++")	
		print("\t>> Here's your code:", colored(result, 'yellow', attrs=['bold']))
		print("\t   +++++++++++++++++++++++++++++++++++++++")
		
		isfileExist = Attributes(uD1, inp, 1, 2, 3, "Time: ", inp3=inp3, 
						 		length=inp4, code='Code:', result=result)
		isfileExist.pherr()

	elif inp2 == n.lower() :
		print("\t+++++++++++++++++++++++++") 
		print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
		print("\t+++++++++++++++++++++++++")

		isfileExist = Attributes(uD2, inp, 1, 2, 3, "Aborting at: ")
		isfileExist.pherr()
		time.sleep(1) 

	else : 
		print("\t+++++++++++++++++++++++++++++++++++++")
		print(colored("\t>> Try again, that's not a valid answer.", 'red', attrs=['bold']))
		print("\t+++++++++++++++++++++++++++++++++++++")

		isfileExist = Attributes(uD3, inp, 1, 2, 3, "Attempting at: ")
		isfileExist.pherr()		

if __name__ == '__main__':
	codeGen()