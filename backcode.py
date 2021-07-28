from srcode import *

class inpClass:

	def __init__(self, inp): 

		self.inp = inp

	def inpf(self):

		self.inp = input("\n\t>> Hi, what's yourname: ")

class attrClass(inpClass):

	def __init__(
		self, ud, inp,
		slp0, slp1, slp2,
		stats, code='', result=''):

		super().__init__(inp)

		self.ud = ud 
		self.slp0 = slp0
		self.slp1 = slp2
		self.slp2 = slp2
		self.stats = stats
		self.code = code
		self.result = result


	def pherr(self):

		print("\t++++++++++++++++++++++++++++")
		print(colored("\t[!] File doesn't exist in the database! ", 'cyan', attrs=['bold']))
		
		time.sleep(self.slp0)
		print(colored("\t[!] Adding " + self.ud + "...", 'cyan', attrs=['bold']))
		
		time.sleep(self.slp1)
		print("\t++++++++++++++++++++++++++++")

		open(self.ud, 'w')

		with open(self.ud) as fp:

			fp.read()
			print({"User: "+ self.inp},
				  {self.code + self.result}, 
				  {self.stats + time.ctime(sec)}, 
				  file=open(self.ud, 'a'))			
			fp.close()

		time.sleep(self.slp2)

		print("\t++++++++++++++++++++++++++++++++++++++++")
		print(colored("\t[+] File " + self.ud + " has been created! ", 'green', attrs=['bold']))
		print("\t++++++++++++++++++++++++++++++++++++++++")