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
def show_high_data():
	command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.data+notation.sort_data_count
	execute=os.popen(command). read()
	line=execute.split("\n")
	j=len(line)
	j=j-2
	a=j
	max_bit=0
	int(max_bit)
	print("No.of Packets\tSource\t\t\tDestination")
	print("=============\t======\t\t\t===========")
	while(j>=0):
                k=line[j]
                bits,source,dest=k.split(",")
		if(int(bits)>max_bit):
			max_bit=int(bits)
		j=j-1
	while(a>=0):
		b=line[a]
		bits1,source1,dest1=b.split(",")
                if(int(bits1)==max_bit):
			print(Fore.RED+Back.BLACK+bits1+"\t\t"+source1+"\t"+dest1+Style.RESET_ALL)
		else:
                	print bits1+"\t\t"+source1+"\t"+dest1
		a=a-1
