#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import urllib
import os
import colorama
from core.forensiclib import fakemaclib
from colorama import Fore, Back, Style
colorama.init()                  	
def show_all_Deauth():
        command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.deauth+notation.sort_deauth
        execute=os.popen(command).read()
	line=execute.split("\n")
	j=len(line)
	j=j-2
	while(j>=0):
		k=line[j]
		num,source,dest=k.split(",")
		smc=fakemaclib.mac_check(source)
		dmc=fakemaclib.mac_check(dest)
		if(smc=="none" or dmc=="none"):
        		print smc+"("+source+")"+" sent "+ str(num)+" De-Auth Packets to "+"Broadcast"+"("+dest+")"
		else:
			print smc+"("+source+")"+" sent "+ str(num)+" De-Auth Packets to "+dmc+"("+dest+")"
		j=j-1

	




	
