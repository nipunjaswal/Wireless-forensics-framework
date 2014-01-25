#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()                  	
j='"'
k='"'
#Show All Successful Authentication Response Module
def runmod():
        command="tshark -r /root/deepak-01.cap -R "+""" "wlan.fc.type_subtype==0x00||wlan.fc.type_subtype==0x01||wlan.fc.type_subtype==0x04||wlan.fc.type_subtype==0x05||wlan.fc.type_subtype==0x08" """+" -T fields -E separator=, -e frame.number -e wlan.fc.type_subtype -e wlan.sa -e wlan.da| tr -s ' ' ','"
        execute=os.popen(command).read()
	line=execute.split("\n")
        j=len(line)
        j=j-2
	a=0
       	while(a<=j):
		k=line[a]
		no,type,sor,dst=k.split(",")
		if(type=="0x08"):
			print sor+" Sends a Probe Packet to "+dst
			a=a+1
			time.sleep(1)
		elif(type=="0x00"):
			print sor+" Sends an Association Request to "+dst
                	a=a+1
			time.sleep(1)
		else:
			a=a+1



	




	
