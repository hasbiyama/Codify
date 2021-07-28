import time
import os
from os import path
import random
import time
from colorama import init
from termcolor import colored

y = "y"
n = "n"

sec = int(time.time())
uD0 = 'username.txt'
uD1 = 'usercode.txt'
uD2 = 'userabort.txt'
uD3 = 'invalidinput.txt'

aL = "allList.txt"
ptoF0 = './rsc'
srcf = os.listdir('./rsc')

os.chdir(ptoF0)
if not path.exists(aL):
	for x in srcf:
		if not x.startswith('allList') and x.endswith('.txt'):
			with open(x) as fn:
				data = fn.read()
				print(data, file=open(aL, 'a'), end='')			
				fn.close()						

		else: pass

else: pass

letters = open(aL, 'r')
ltr = letters.read()
result = "".join((random.choice(ltr)) for x in range(10))
letters.close()