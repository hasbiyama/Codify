from srcode import *

class Rmforl:

	def __init__(self, opt1, file=''):
		
		self.opt1 = opt1
		self.file = file

	def frLoop(self): 

		os.chdir("../data")

		with open(self.file,'r') as f:
			
			lines = f.readlines()

		with open(self.file,'w') as file:

			print(colored("\t[-] Removing ... \n", 'red', attrs=['bold']))

			time.sleep(2)

			for line in lines:

				if line.find(str(self.opt1)) != -1:

					pass
				
				else:

					file.write(line)

if __name__ == '__main__':
	frLoop()




		
