import re
import os
import sys
import time
import random
from os import path
from datetime import datetime
from colorama import init
from termcolor import colored

y, n = 'y', 'n'
a, b, c, d = 'a', 'b', 'c', 'd'

uD0 = 'username.txt'
uD1 = 'usercode.txt'
uD2 = 'userabort.txt'
uD3 = 'invalid_input.txt'

sec = int(time.time())
now = datetime.now()
cr_time = int(now.strftime("%H"))
DN_TIME = ['Morning', 'Afternoon', 'Evening', 'Night']

aL = "allList.txt"
ptoF0 = './rsc'
srcf = os.listdir('./rsc')

inp = input("\n\t[?] Hi, what's yourname? ->  ")

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
letters.close()
