#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
def show_all_destination():
	command=notation.libc+ " -r "+notation.pack_file+notation.sortd
	print("Destinations")
	print("============")
	execute=os.popen(command).read()
	print(execute)
def show_all_source():
	print("Sources")
        print("=======")
	command=notation.libc+ " -r "+notation.pack_file+notation.sorts
	execute=os.popen(command).read()
	print(execute)

def show_all_association_requests():
	command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.associations_req + notation.sort_source_dest
	execute=os.popen(command).read()
	print execute
	source,dest=execute.split(",")
	print"Source"+"\t\t\t\t\t\t"+"Destination"
	print source+"\t\t====>\t\t"+dest
	
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


		




	
