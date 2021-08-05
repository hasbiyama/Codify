from srcode import *

class File:

	def __init__(self, opt1, file=''):
		
		self.opt1 = opt1
		self.file = file

	def removeFromFile(self): 

		os.chdir("../data")

		total = 0

		with open(self.file,'r') as f:
			
			lines = f.readlines()

		with open(self.file,'w') as file:

			print(colored("\t[-] Removing ... \n", 'red', attrs=['bold']))

			time.sleep(2)

			for line in lines:

				if line.find(str(self.opt1)) != -1:

					pass
				
				else:

					total += 1

					time.sleep(1)

					file.write(line)

			print(colored("\t[+] Remain: " + str(total), 'yellow', attrs=['bold']))


if __name__ == '__main__':
	removeFromFile()




		
