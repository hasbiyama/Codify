from mFile import *

ptoF1 = '../data'
os.chdir(ptoF1)

def codeGen():

	init()
	
	inp = input("\n\t>> Hi, what's yourname: ")
	print("\t***************************")
	print("\t>> Hello, " +  colored(str(inp).upper(), 'magenta', attrs=['bold']) + "!")
	print("\t***************************")

	if not path.exists(uD0):
		
		print("\t++++++++++++++++++++++++++++")
		print(colored("\t[!] File doesn't exist in the database! ", 'cyan', attrs=['bold']))
		time.sleep(1)
		print(colored("\t[!] Adding" + uD0 + "...", 'cyan', attrs=['bold']))
		time.sleep(2)
		print("\t++++++++++++++++++++++++++++")

		open(uD0, 'w')

		with open(uD0) as fp:

			fp.read()
			print({"User: "+ inp}, 
				  {"Login at: " + time.ctime(sec)}, 
				  file=open(uD0, 'a'))			
			fp.close()

		time.sleep(3)

		print("\t++++++++++++++++++++++++++++++++++++++++")
		print(colored("\t[+] File " + uD0 + " has been created! ", 'green', attrs=['bold']))
		print("\t++++++++++++++++++++++++++++++++++++++++")

	elif path.exists(uD0):

		with open(uD0) as fp:

			fp.read()
			print({"User: "+ inp}, 
				  {"Login at: " + time.ctime(sec)}, 
				  file=open(uD0, 'a'))			
			fp.close()

	else: pass

	inp2 = input("\n\t>> Would you like to generate your code? \n\t(y/n) : ")

	if inp2 == y.lower():

		print("\t+++++++++++++++++++++++++++")	
		print("\t>> Your code is:", colored(result, 'yellow', attrs=['bold']))
		print("\t+++++++++++++++++++++++++++")
		
		if not path.exists(uD1):

			print("\t+++++++++++++++++++++++++")
			print(colored("\t[!] File doesn't exist in the database! ", 'cyan', attrs=['bold']))
			time.sleep(1)
			print(colored("\t[!] Adding " + uD1 + "...", 'cyan', attrs=['bold']))
			time.sleep(2)
			print("\t+++++++++++++++++++++++++")

			open(uD1, 'w')

			with open(uD1) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Code: " + result},
					  {"Time: " + time.ctime(sec)}, 
					  file=open(uD1, 'a'))			
				fp.close()

			time.sleep(3)

			print("\t++++++++++++++++++++++++++++++++++++++++")
			print(colored("\t[+] File " + uD1 + " has been created! ", 'green', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++++++")


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

			print("\t+++++++++++++++++++++++++")
			print(colored("\t[!] File doesn't exist in the database! ", 'cyan', attrs=['bold']))
			time.sleep(1)
			print(colored("\t[!] Adding " + uD2 + "...", 'cyan', attrs=['bold']))
			time.sleep(2)
			print("\t+++++++++++++++++++++++++")

			open(uD2, 'w')

			with open(uD2) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Aboting at: " + time.ctime(sec)}, 
					  file=open(uD2, 'a'))			
				fp.close()

			time.sleep(2)

			print("\t++++++++++++++++++++++++++++++++++++++++")
			print(colored("\t[+] File " + uD2 + " has been created! ", 'green', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++++++")


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

			print("\t+++++++++++++++++++++++++")
			print(colored("\t[!] File doesn't exist in the database! ", 'cyan', attrs=['bold']))
			time.sleep(1)
			print(colored("\t[!] Adding " + uD3 + "...", 'cyan', attrs=['bold']))
			time.sleep(2)
			print("\t+++++++++++++++++++++++++")

			open(uD3, 'w')

			with open(uD3) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Attempting at: " + time.ctime(sec)}, 
					  file=open(uD3, 'a'))			
				fp.close()

			time.sleep(3)

			print("\t++++++++++++++++++++++++++++++++++++++++")
			print(colored("\t[+] File " + uD3 + " has been created! ", 'green', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++++++")

		elif path.exists(uD3):

			with open(uD3) as fp:

				fp.read()
				print({"User: "+ inp}, 
					  {"Attempting at: " + time.ctime(sec)}, 
					  file=open(uD3, 'a'))			
				fp.close()

		else: pass			

codeGen()