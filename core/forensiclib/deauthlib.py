#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import urllib
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()                  	
def show_all_Deauth():
        command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.deauth+notation.sort_source_dest
        execute=os.popen(command).read()
	line=execute.split("\n")
	j=len(line)
	j=j-2
    	print"Source"+"\t\t\t\t\t\t"+"Destination"
	while(j>=0):
		k=line[j]
		source,dest=k.split(",")
        	print source+"\t\t====>\t\t"+dest
		j=j-1

	




	
