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
j='"'
k='"'
#Show All Successful Authentication Response Module
def show_all_association_response():
        command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.success_auth+ notation.sort_auth
        execute=os.popen(command).read()
        line=execute.split("\n")
        j=len(line)
        j=j-2
        print"Source ====> Destination"
        while(j>=0):
                k=line[j]
                source,dest,mon,date,year,time=k.split(",")
                print dest+" ====> "+source+" ====> "+time
                j=j-1


	




	
