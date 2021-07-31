import rmdir_ext
import backcode
from condt import *
from srcode import *
from codegen import codeGen
from codegen import inputPart

class Remdir(Conditional):

	def __init__(self, inp, arg=''): 
		
		super().__init__(inp, arg)
		
	def remDir(self):

		if path.exists("../data"):

			rmdir_ext.Remdirext().ifExt()

		elif not path.exists("../data"):

			print(colored("\n\t[!] Data folder doesn't exist.", 'red', attrs=['bold']))

			time.sleep(2)
			
			print(colored("\n\t[*] Creating ./data ... ", 'green', attrs=['bold']))
			
			time.sleep(2)
			
			os.makedirs("../data")

			print(colored("\n\t[+] ./data created!\n", 'yellow', attrs=['bold']))

			os.chdir("../data")

			# USERNAME.TXT

			backcode.Attributes(uD0, inp, 1, 2, 3, "Login at: ").pherr() 

			# USERCODE.TXT

			isfileExist = backcode.Attributes(uD1, inp, 1, 2, 3, "Time: ", code='Code: ')
			isfileExist.pherr()

			# USERABORT.TXT

			backcode.Attributes(uD2, inp, 1, 2, 3, "Aborting at: ").pherr() 

			# INVALID INPUT.TXT

			backcode.Attributes(uD3, inp, 1, 2, 3, "Attempting at: ").pherr()		

			rmdir_ext.Remdirext().ifExt()
			# sys.exit()

		else: pass

if __name__ == '__main__':
	remDir()