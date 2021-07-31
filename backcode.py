from srcode import *

class Input:

	def __init__(self, inp, inp3, length): 

		self.inp = inp
		self.inp3 = inp3
		self.length =length

class Attributes(Input):

	def __init__(
		self, ud, inp, slp0, 
		slp1, slp2,stats, inp3='',
		length='', code='', result=''):

		super().__init__(inp, inp3, length)

		self.ud = ud 
		self.slp0 = slp0
		self.slp1 = slp2
		self.slp2 = slp2
		self.stats = stats
		self.code = code
		self.length = length
		self.result = result

	def pherr(self):

		if not path.exists(self.ud):

			print("\t++++++++++++++++++++++++++++")
			print(colored("\t[!] File doesn't exist in the database! ", 'cyan', attrs=['bold']))
			
			time.sleep(self.slp0)
			print(colored("\t[!] Adding " + self.ud + "...", 'cyan', attrs=['bold']))
			
			time.sleep(self.slp1)
			print("\t++++++++++++++++++++++++++++")

			open(self.ud, 'w')

			with open(self.ud) as fp:

				lines = fp.readlines()
				
				count = 0
				for line in lines:
					count += 1

				print(f'[line {count}] <{"user: "+ self.inp}> <{"org: " + self.inp3}> <{"len: "+ self.length}> <{self.code + self.result}> <{self.stats + time.ctime(sec)}>', file=open(self.ud, 'a'))
							
				fp.close()


			time.sleep(self.slp2)

			print("\t++++++++++++++++++++++++++++++++++++++++")
			print(colored("\t[+] File " + self.ud + " has been created!", 'green', attrs=['bold']))
			print("\t++++++++++++++++++++++++++++++++++++++++\n")
	
		elif path.exists(self.ud):

			with open(self.ud) as fp:

				lines = fp.readlines()
				
				count = 0
				for line in lines:
					count += 1

				print(f'[line {count}] <{"user: "+ self.inp}> <{"org: " + self.inp3}> <{"len: "+ self.length}> <{self.code + self.result}> <{self.stats + time.ctime(sec)}>', file=open(self.ud, 'a'))
									
				fp.close()

		else: pass	
if __name__ == '__main__':
	pherr()