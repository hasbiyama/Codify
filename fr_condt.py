from srcode import *

class ForL:

	def __init__(self, opt1, file=''):
		
		self.opt1 = opt1
		self.file = file

	def frLoop(self):

		pattern = re.compile(self.opt1)

		for i, line in enumerate(open(self.file)):
			
			for match in re.finditer(pattern, line):
				
				print(colored("\t[*] Found!\n", 'green', attrs=['bold']))
				
				print("   " + match.string)
				
				sys.exit()
		
		sys.exit()

if __name__ == '__main__':
	frLoop()
	