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
	print("No.of Packets\t\tSource\t\t\t\t\tDestination")
        print("=============\t\t======\t\t\t\t\t===========")
	while(j>=0):
		k=line[j]
		num,source,dest=k.split(",")
		smc=fakemaclib.mac_check(source)
		dmc=fakemaclib.mac_check(dest)
		if(dmc=="none" and dest!="ff:ff:ff:ff:ff:ff"):
        		print(num+"\t\t\t"+source+"\t\t"+dest+"(Suspicious)"+Style.RESET_ALL)
		elif(dest=="ff:ff:ff:ff:ff:ff"):
			print(Style.DIM+num+"\t\t\t"+source+"\t\t\t"+dest+"(Broadcast)"+Style.RESET_ALL)
		else:
			print(Fore.RED+Style.BRIGHT+num+"\t\t\t"+source+"("+smc+")"+"\t\t"+dest+"("+dmc+")"+Style.RESET_ALL)
		j=j-1



	
