import option_opr
from srcode import *

class Verify:

	def __init__(self, outter_inp):

		self.outter_inp = outter_inp

	def verifyCode(self):

		inner_inp = input("\n\t[!] Please type your code : ")

		if inner_inp == "":

			time.sleep(1)
			
			print(colored("\n\t[x] This line cannot be empty!", 'red', attrs=['bold']))
		
			sys.exit()

		else:

			with open(uD1, 'r') as f:

				fp = str(f.readlines())

				# for line in fp:
			
				if re.search(r'\bCode: {}\b'.format(inner_inp), fp):

					print(colored("\n\t[*] Logging in ...", 'green', attrs=['bold']))

					time.sleep(1) 

					option_opr.Exists().dataExists()

				else:

					time.sleep(2)

					print(colored("\n\t[x] Cannot find -> " + colored("user: " + self.outter_inp, 'yellow') + " | " + colored("code: " + inner_inp, 'yellow'), 'red', attrs=['bold']))

					time.sleep(1)	
					
					sys.exit()

if __name__ == '__main__':
	verifyCode()
