from srcode import *

class Remdir():

	def __init__(self, arg='', curr_time=cr_time):

		self.arg = arg
		self.curr_time = curr_time
		
	def remDir(self):
		for x in srcf0:
			if x.endswith('.txt'):
				if self.curr_time in range(3, 11):
					self.arg = (DN_TIME[0])

				elif self.curr_time in range(11, 14):
					self.arg = (DN_TIME[1])

				elif self.curr_time in range(14, 19):
					self.arg = (DN_TIME[2])

				elif self.curr_time in range(19, 3):
					self.arg = (DN_TIME[3])

				else: pass

			elif not x.endswith('.txt'): 
				
				inpNew = input("\n\t>> No database files! What you gonna do:\n\t  (a) Create | (b) Exit ->  ")

				if inpNew == a: 
					pass

				elif inpNew == b:

					print("\t+++++++++++++++++++++++++") 
					print(colored("\t[-] Aborting ... bye!", 'green', attrs=['blink']))
					print("\t+++++++++++++++++++++++++")

					isfileExist = Attributes(uD2, inp, 1, 2, 3, "Aborting at: ")
					isfileExist.pherr()	
					# time.sleep(1) 				
					os.abort()

				else: pass

			else: pass