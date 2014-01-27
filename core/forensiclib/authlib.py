#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
import warnings
warnings.filterwarnings('ignore')
import colorama
import time
from colorama import Fore, Back, Style
colorama.init()                  	
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

def show_failed_attempts():
	warnings.filterwarnings('ignore')
	command=notation.libc+ " -r " + notation.pack_file+" -R"+notation.auth_deauth+ notation.sort_auth_deauth
	execute=os.popen(command).read()
	line=execute.split("\n")
        j=len(line)
        j=j-2
	count=0
	summer=0
	at=0
        while(count<=j):
                k=line[count]
                source,dest,type,frame,mon,date,year,time=k.split(",")
		if(summer!=10001):
			if(type=="0x0b"):
				summer=summer+5000	
				count=count+1
			else:
				summer=summer+1
				if(summer==10001):
					comm=notation.libc+ " -r "+notation.pack_file+" -R "+"frame.number=="+frame+notation.frame
					execute2=os.popen(comm).read()
					execute2= execute2 [:6]
					if(execute2=="0x0006"):
						print Style.DIM+source+"==================>"+dest+"=============>"+time+"(Due To Failed Attempt)"+Style.RESET_ALL
						summer=0
					elif(execute2=="0x0003"):
						print Fore.RED+Style.BRIGHT+source+"==================>"+dest+"=============>"+time+"(Intentional DE-AUTH)"+Style.RESET_ALL	
						summer=0
				count=count+1

	
