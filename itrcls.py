import filecls
from srcode import *

class Itter:

	def __init__(self, cr_time): 

		self.cr_time = cr_time

	def elseIf(self):

		if self.cr_time in range(3, 11): 
			filecls.Func(inp, DN_TIME[0]).fileFunc()

		elif self.cr_time in range(11, 14): 
			filecls.Func(inp, DN_TIME[1]).fileFunc()

		elif self.cr_time in range(14, 19): 
			filecls.Func(inp, DN_TIME[2]).fileFunc()

		elif self.cr_time in range(19, 24): 
			filecls.Func(inp, DN_TIME[3]).fileFunc()

		elif self.cr_time in range(0, 3):
			filecls.Func(inp, DN_TIME[3]).fileFunc()
		else:
			pass

if __name__ == '__main__':
	elseIf()