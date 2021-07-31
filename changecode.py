import backcode
import rm_fr_condt
from srcode import *

def retype():


# RETYPING CODE


	inp0 = input("\n\t[*] Please re-type your name -> \n")

	with open('username.txt', 'r') as f:

		for lsl in f: pass

		lsn = lsl

	if inp0 in lsn:

		rm_fr_condt.Rmforl(inp0, file=uD1).frLoop()

	else: 

		print(colored("\n\t[!] Please type your name correctly", 'red', attrs=['bold']))
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

		print("\t   ++++++++++++++++")	
		print("\t>> Hey, yo!")
		print("\t   Here's your code:", colored(result, 'yellow', attrs=['bold']))
		print("\t   ++++++++++++++++\n")

		print(colored("\t[!] have a nice day ~", 'green', attrs=['bold']))

		isfileExist = backcode.Attributes(uD1, inp0, 1, 2, 3, "Time: ", inp3=inp3, 
										length=inp4, code='Code: ', result=result)
		isfileExist.pherr()

		time.sleep(1)

		sys.exit()



if __name__ == '__main__':
	retype()