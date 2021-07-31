from srcode import *

class Initialiser:

	def __init__(self, inp='') : 

		self.inp = inp

	def greets(self):

		print("\n\t[*] Since this is your first time, I'll guide you :)")
		
		time.sleep(2)
		
		print("\t[*] Please input " + colored('admin', 'yellow', attrs=['bold']) + " for the name, and I will generate everything for you!")
		
		time.sleep(2)

	def adminAdd(self):

		if self.inp.lower() == "admin": 

			print("\n\t[*] Please wait and enjoy Codify ;)")
			
			time.sleep(1)

		else:

			print("\n\t[!] I'm sorry, you are not registered.")
			
			print("\t     Please ask a member or admin to add you.")
			
			time.sleep(1)
			
			sys.exit()

if __name__ == '__main__':
	greets()