from srcode import *
import time
from colorama import init
from termcolor import colored

def codeGen():

	init()

	y = "y"
	n = "n"
	sec = int(time.time())
	uD = 'userdatas.txt'

	letters = open(aL, 'r')
	ltr = letters.read()
	result = "".join((random.choice(ltr)) for x in range(10))
	letters.close()
	
	inp = input("\n\tHi, what's yourname: ")
	print("\t+++++++++++++++++++++++++")
	print("\tHello, " +  colored(str(inp), 'magenta', attrs=['bold']) + "!")
	print("\t+++++++++++++++++++++++++")

	inp2 = input("\n\tWould you like to generate your code? \n\t(y/n) : ")

	if inp2 == y.lower():
		print("\t+++++++++++++++++++++++++++")	
		print("\tYour code is:", colored(result, 'yellow', attrs=['bold']))
		print("\t+++++++++++++++++++++++++++")
		
		if not path.exists(uD):
			open(uD, 'w')
		elif path.exists(uD):
			with open(uD) as fp:
				fp.read()
				print({"User: "+ inp}, {"Code: " + result},
						{"time: " + time.ctime(sec)}, file=open(uD, 'a'))			
				fp.close()
		else: pass	

	elif inp2 == n.lower() :
		print("\t+++++++++++++++++++++++++") 
		print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
		print("\t+++++++++++++++++++++++++")
		time.sleep(2) 

	else : 
		print("\t+++++++++++++++++++++++++++++++++++++")
		print(colored("\tTry again, that's not a valid answer.", 'red', attrs=['bold']))
		print("\t+++++++++++++++++++++++++++++++++++++")

codeGen()