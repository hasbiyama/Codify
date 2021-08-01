import searching_db
from srcode import *

class Search:

	def __init__(self, opt):

		self.opt = opt

	def db_Search(self):

		print("\n\t[?] Type a user or time (e.g. 'Albert' or 'Thu Jul 29'):\n")
		
		inpSp1 = input("\t>>  ")
		
		print("")

		if inpSp1 == "" :
	
			print(colored("\t[x] This line cannot be empty!", 'red', attrs=['bold']))
	
			sys.exit()

		else: pass

		# searching input

		if self.opt == a:
			searching_db.File(inpSp1, file=uD0).searchFromFile()


		elif self.opt == b:
			searching_db.File(inpSp1, file=uD1).searchFromFile()


		elif self.opt == c:
			searching_db.File(inpSp1, file=uD3).searchFromFile()
	
		
		elif self.opt == d:
			searching_db.File(inpSp1, file=uD2).searchFromFile()

		elif self.opt == e:
			searching_db.File(inpSp1, file=uD4).searchFromFile()

if __name__ == '__main__':
	optFunc()

