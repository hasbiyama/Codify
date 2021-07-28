from srcode import *
from backcode import attrClass
from backcode import inpClass

ptoF1 = '../data'
os.chdir(ptoF1)

def codeGen():

	init()

	inp = input("\n\t>> Hi, what's yourname: ")

	print("\t***************************")
	print("\t>> Hello, " +  colored(str(inp).upper(), 'magenta', attrs=['bold']) + "!")
	print("\t***************************")

	if not path.exists(uD0):
		
		usrr = attrClass(uD0, inp, 1, 2, 3, "Login at: ")
		usrr.pherr()

	elif path.exists(uD0):

		with open(uD0) as fp:

			fp.read()
			print({"User: "+ inp}, 
				  {"Login at: " + time.ctime(sec)}, 
				  file=open(uD0, 'a'))			
			fp.close()

	else: pass

	inp2 = input("\n\t>> Would you like me to generate your code? \n\t(y/n) : ")

	if inp2 == y.lower():

		print("\t==========================================")	
		inp3 = input("\n\t>> What is the str, num, or char do you want me to codify:\n\t>> ")
		print("\t==========================================================")	
		inp4 = input("\n\t>> How long is your desired code: ")
		print("\t=======================================")	

		result = "".join((random.choice(inp3).join((random.choice(ltr)) for x in range(int(inp4)))))

		print("\t+++++++++++++++++++++++++++")	
		print("\t>> Here's your code:", colored(result, 'yellow', attrs=['bold']))
		print("\t+++++++++++++++++++++++++++")
		
		if not path.exists(uD1):

			usrr = attrClass(uD1, inp, 1, 2, 3, "Time: ", code='Code:', result=result)
			usrr.pherr()

		elif path.exists(uD1):

			with open(uD1) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Code: " + result},
					  {"Time: " + time.ctime(sec)}, 
					  file=open(uD1, 'a'))			
				fp.close()

		else: pass	

	elif inp2 == n.lower() :
		print("\t+++++++++++++++++++++++++") 
		print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
		print("\t+++++++++++++++++++++++++")
		
		if not path.exists(uD2):

			usrr = attrClass(uD2, inp, 1, 2, 3, "Aborting at: ")
			usrr.pherr()

		elif path.exists(uD2):

			with open(uD2) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Aboting at: " + time.ctime(sec)}, 
					  file=open(uD2, 'a'))			
				fp.close()

		else: pass			

		time.sleep(1) 

	else : 
		print("\t+++++++++++++++++++++++++++++++++++++")
		print(colored("\t>> Try again, that's not a valid answer.", 'red', attrs=['bold']))
		print("\t+++++++++++++++++++++++++++++++++++++")

		if not path.exists(uD3):

			usrr = attrClass(uD3, inp, 1, 2, 3, "Attempting at: ")
			usrr.pherr()

		elif path.exists(uD3):

			with open(uD3) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Attempting at: " + time.ctime(sec)}, 
					  file=open(uD3, 'a'))			
				fp.close()

		else: pass			

codeGen()