from srcode import *
import file_create_add


class Generator:


	def __init__(self, inp=''):

		self.inp = inp


	# REGENERATING CODE


	def reGen(self):


		# INPUT CODE


		inp2 = input("\t[?] Would you like me to regenerate the code? (y/n) : ")

		inp2.replace(" ", " ")

		print("")


		# ORIGINAL INPUT 


		if inp2.lower() == y:

			print("\t[?] What do you want me to codify?" + colored(' *len_min: 6 ', 'grey', attrs=['bold']) + "-> ", end='')
			
			inp3 =  input("")

			inp3.replace(" ", " ")		
			
			print("")

			if inp3 == "":

				print(colored("\t[x] The input must not empty!", 'red', attrs=['bold']))
			
				sys.exit()     

			elif len(inp3) <= 5:

				time.sleep(1)

				print(colored("\t[!] Your code length is < 6 ", 'red', attrs=['bold']))
			
				sys.exit()     

			else: pass


			# LENGTH ORIGINAL INPUT


			print("\t[?] How long is your code length?" + colored(' *min: 6 ', 'grey', attrs=['bold']) + "-> ", end='' )

			inp4 = input("")

			inp4.replace(" ", " ")
			
			print("")

			if inp4 == "":

				print(colored("\t[x] Please input your code length!", 'red', attrs=['bold']))
			
				sys.exit()


			# LENGTH GENERATED INPUT


			elif not re.findall(r'\d', inp4):

				time.sleep(1)

				print(colored("\t[x] Please input an integer!", 'red', attrs=['bold']))
			
				sys.exit()

			elif int(inp4) <= 5:

				time.sleep(1)

				print(colored("\t[!] {} < 6 ", 'red', attrs=['bold']).format(inp4))
			
				sys.exit()                                   

			else: pass


			# GENERATING CODE


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

			
			isfileExist = file_create_add.Attributes(uD1, self.inp, 1, 2, 3, "Time: ", inp3=inp3, 
											length=inp4, code='Code: ', result=result)
			isfileExist.createFile()

			sys.exit()


		# NEITHER IN CODE NOR USER


		elif inp2.lower() == n :

			print("\n\t+++++++++++++++++++++++++") 
			print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
			print("\t+++++++++++++++++++++++++")

			file_create_add.Attributes(uD2, self.inp, 1, 2, 3, "Aborting at: ").createFile() 

			time.sleep(1)

			sys.exit()

		else : 
			print("\t++++++++++++++++++++++++++++++++++++++++")
			print(colored("\t[x] Try again, that's not a valid answer", 'red', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++++++")

			file_create_add.Attributes(uD3, self.inp, 1, 2, 3, "Attempting at: ").createFile()		

			time.sleep(1)

			sys.exit()

if __name__ == '__main__':
	reGen()
