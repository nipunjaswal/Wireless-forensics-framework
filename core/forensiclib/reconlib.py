#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
from core.forensiclib import fakemaclib
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()                  	
def runmod():
        command=notation.libc+" -r "+ notation.pack_file +" -R "+ notation.recon_packet+ notation.sort_recon
        execute=os.popen(command).read()
	line=execute.split("\n")
        j=len(line)
        j=j-2
	a=0
       	while(a<=j):
		k=line[a]
		no,type,sor,dst,month,date,year,time=k.split(",")
		source_mac_check=fakemaclib.mac_check(sor)
		dest_mac_check=fakemaclib.mac_check(dst)	
		if(type=="0x08"):
			print source_mac_check+"("+sor+")"+"Sends a Beacon Frame to "+"("+dst+")"+dest_mac_check+ " at "+time
			a=a+1
		elif(type=="0x00"):
			print Fore.MAGENTA+source_mac_check+"("+sor+")"+"Sends an Association request to "+"("+dst+")"+dest_mac_check+ " at "+time+Style.RESET_ALL
                	a=a+1
		elif(type=="0x01"):
			print source_mac_check+"("+sor+")"+"Sends a Association response to "+"("+dst+")"+dest_mac_check+ " at "+time
                        a=a+1
		elif(type=="0x04"):
                        print source_mac_check+"("+sor+")"+"Sends a Probe request to "+"("+dst+")"+dest_mac_check+ " at "+time
                        a=a+1
		elif(type=="0x05"):
                        print source_mac_check+"("+sor+")"+"Sends a Probe response to "+"("+dst+")"+dest_mac_check+ "at "+time
                        a=a+1
		else:
			a=a+1


	




	
