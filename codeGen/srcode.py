import os
from os import path
import random

aL = "allList.txt"
ptoF = './rsc'
srcf = os.listdir('./rsc')

if not path.exists(aL):
	os.chdir(ptoF)
	for x in srcf:
		if not x.startswith('allList') and x.endswith('.txt'):
			with open(x) as fn:
				data = fn.read()
				print(data, file=open(aL, 'a'), end='')			
				fn.close()						

		else:
			with open(aL, 'r+') as fn:
				fn.truncate()
				for x in srcf:
					if not x.startswith('allList') and not x.startswith('userdatas') and x.endswith('.txt'):
						data = fn.read()
						print(data, file=open(aL, 'a'), end='')
		fn.close()

else: pass


