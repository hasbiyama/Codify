from srcode import *

class Guide:

	def __init__(self, inp='') : 

		self.inp = inp

	def greets(self):

		print("\n\t[*] Since this is your first time, I'll guide you :)")
		
		time.sleep(2)
		
		print("\t[*] Please type " + colored('admin', 'yellow', attrs=['bold']) + " [@id: 1] for the name, and I will generate everything for you!")
		
		time.sleep(2)

	def adminAdd(self):

		if self.inp.lower() == "admin": 

			print("\n\t[*] Please wait and enjoy Codify ;)")
			
			time.sleep(1)

		else:

			print(colored("\n\t[!] I'm sorry, you are not registered.", 'yellow', attrs=['bold']))
			
			print(colored("\t    Please ask a member or admin to add you.", 'cyan', attrs=['bold']))
			
			time.sleep(1)
			
			sys.exit()

if __name__ == '__main__':
	greets()