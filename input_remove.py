import remove_db 
from srcode import *

class Remove:

	def __init__(self, opt):

		self.opt = opt

	def db_Remove(self):

		print("\n\t[?] Type a user and/or time (e.g. 'Albert' or 'Thu Jul 29'):\n")
		
		inpSp1 = input("\t>>  ")
		
		print("")

		if inpSp1 == "" :
		
			print(colored("\t[x] This line cannot be empty!", 'red', attrs=['bold']))
		
			sys.exit()

		else: pass

		if self.opt == a:
			remove_db.File(inpSp1, file=uD0).removeFromFile()


		elif self.opt == b:
			remove_db.File(inpSp1, file=uD1).removeFromFile()


		elif self.opt == c:
			remove_db.File(inpSp1, file=uD2).removeFromFile()
	
		
		elif self.opt == d:
			remove_db.File(inpSp1, file=uD3).removeFromFile()

		
		elif self.opt == e:
			remove_db.File(inpSp1, file=uD4).removeFromFile()


if __name__ == '__main__':
	db_Remove()