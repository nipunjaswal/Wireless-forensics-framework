#!/usr/bin/env python
#Importing System Files for Using OS based Functions
import os
import re
from conf import notation
import time
import warnings
warnings.filterwarnings('ignore')
import colorama
import time
from colorama import Fore, Back, Style
colorama.init()
def findap():
	ap='""" "DLinkVWR" """'
	command=notation.find+apval
	print command
	k=100
	while(int(k)>10):
		yo=os.popen(command).read()
		#Separating the Output
		signal,ssid=yo.split(",")
		#Removing Additional Spaces
		newssid=ssid.strip()
		newsignal=signal.strip()
		#Finding Digits
		digits=re.findall(r'\d+',newsignal)
		#Finding the Sum up value
		k=digits[0]
		#Limits
		high=10
		med=25
		low=50
		#Finding the AP
		print k 
		if(int(k)<=int(high)):
			print("Router Within 5 Feet")
			break
		elif(int(k)>int(high) and int(k)<=int(med)):
			print("Router Nearby within 10 to 25 feet Change Direction and for 5 Seconds")
			time.sleep(5)
		elif(int(k)>int(med) and int(k)<=int(low)):
                        print("Router Nearby within 25 to 50 feet Change Direction and for 5 Seconds")
		else:
			print("Router Quite Far")
		continue



