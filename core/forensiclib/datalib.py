#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
from core.forensiclib import fakemaclib
def show_high_data():
	command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.data+notation.sort_data_count
	execute=os.popen(command). read()
	line=execute.split("\n")
	j=len(line)
	j=j-2
	a=j
	max_bit=0
	int(max_bit)
	print("No.of Packets\tSource\t\t\t\tDestination")
	print("=============\t======\t\t\t\t===========")
	while(a>=0):
		b=line[a]
		bits1,source1,dest1=b.split(",")
		if(source1=="01:00:5e:00:00:01" or source1=="01:00:5e:00:00:02" or source1=="01:00:5e:00:00:01" or source1=="33:33:00:00:00:fb" or source1=="33:33:00:00:00:02" or source1=="33:33:00:00:00:01" or source1=="01:00:5e:00:00:fb" or source1=="01:00:5e:7f:ff:fa"):
                	print(Style.DIM+bits1+"\t\t"+dest1+"\t\t"+source1+"(MultiCast)"+Style.RESET_ALL)
		elif(source1=="ff:ff:ff:ff:ff:ff"):
			print(Style.DIM+bits1+"\t\t"+dest1+"\t\t"+source1+"(Broadcast)"+Style.RESET_ALL)
		else:	
			dest=fakemaclib.mac_check(dest1)
			sour=fakemaclib.mac_check(source1)
			print Fore.RED+Style.BRIGHT+bits1+"\t\t"+dest1+"("+dest+")"+"\t"+source1+"("+sour+")"+Style.RESET_ALL
		a=a-1
