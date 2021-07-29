import time
import sys
import os
from os import path
import pyautogui
import random
import time
from datetime import datetime
from colorama import init
from termcolor import colored

y = "y"
n = "n"
a, b, c, d = 'a', 'b', 'c', 'd'
num = 0

uD0 = 'username.txt'
uD1 = 'usercode.txt'
uD2 = 'userabort.txt'
uD3 = 'invalidinput.txt'
invalid = 'invalidiput.txt'
abort = 'userabort.txt'
codes = 'usercode.txt'
user = 'username.txt' 

sec = int(time.time())
now = datetime.now()
cr_time = now.strftime("%H")
DN_TIME = ['Morning', 'Afternoon', 'Evening', 'Night']

aL = "allList.txt"
ptoF0 = './rsc'
srcf = os.listdir('./rsc')
srcf0 = os.listdir('./data')	

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
