import remove_db
import generate_code
import file_create_add
from srcode import *

def reType():

# RETYPING CODE

	inp0 = input("\n\t[*] Please re-type your name -> ")
	print("")


	with open(uD4, 'r') as f:

		fp = f.readlines()

		for lsl in fp: pass

		if inp0 in lsl:

			time.sleep(1)

			remove_db.File(inp0, file=uD1).removeFromFile()

			time.sleep(1)

		else: 

			time.sleep(2)

			print(colored("\t[!] Please type your name correctly", 'red', attrs=['bold']))
			time.sleep(1)
			sys.exit()

	generate_code.Generator(inp=inp0).reGen()

if __name__ == '__main__':
	reType()