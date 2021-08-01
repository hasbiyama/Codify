from srcode import *

class File:

	def __init__(self, opt1, file=''):
		
		self.opt1 = opt1
		self.file = file

	def searchFromFile(self):

		os.chdir("../data")

		total = 0

		pattern = re.compile(self.opt1)

		for i, line in enumerate(open(self.file)):
			
			for match in re.finditer(pattern, line):

				total += 1
				
				print(colored("\t[*] Found!\n", 'green', attrs=['bold']))
				
				print("   " + match.string)

				time.sleep(1)

		print(colored("\t[+] Total: " + str(total), 'yellow', attrs=['bold']))
				
				# sys.exit()
		
		sys.exit()

if __name__ == '__main__':
	frLoop()
	 