from srcode import *
from rmdir import *

ptoF1 = '../data'
os.chdir(ptoF1)

class Conditional(Remdir):

	def __init__(self, users):

		self.users = users
		super().__init__()
		rmdir = Remdir()
		rmdir.remDir()

	def greetings(self):

		print("\n\t>> Good " + self.arg + ", " + colored(str(self.users).upper(), 'magenta', attrs=['bold']) + "!")
		print("\t   ***************************")
		print("\n\t>> Database files are exist! What you gonna do?\n")
		inputGr = input("\t>> (a) Erase | (b) Append | (c) Access : ->  ")
		print("\t   *****************************************************")

		if inpGr == a:
			os.remove('.')
		
		elif inpGr == b: 
			pass

		elif inpGr == c: 
			
			print("\t>> What do you want to find? ")
			inputSp = input("\t>> (a) users | (b) codes | (c) invalid login | (d) abort opr ->  ")
			print("\t   ==========================================================")
			print("\t >> Type a user or time\n")
			inpSp1 = input("\t>> (e.g. Thu Jul 29 13:23:32 2021) : \n\t  ")
			print("\t   =======================================")

			while i in srcf0:
				try:
					if inpSp == a:
						with open(user) as f:
							if inpSp1 in f.readline():
								print(f.readline())

					if inpSp == b:
							with open(codes) as f:
								if inpSp1 in f.readline():
									print(f.readline())		

					if inpSp == c:
							with open(invalid) as f:
								if inpSp1 in f.readline():
									print(f.readline())	

					if inpSp == d:
							with open(abort) as f:
								if inpSp1 in f.readline():
									print(f.readline())	

					else: 
						print("\t+++++++++++++++++++++++++++++++++++++")
						print(colored("\t>> Try again, that's not a valid answer.", 'red', attrs=['bold']))
						print("\t+++++++++++++++++++++++++++++++++++++")
						time.sleep(1)
						sys.exit()

				except : pass





		







