#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
# Statistics Module For Finding Start time End Time And Duration
from conf import stats
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
#Finding the Start Time of The Capture
def capstart():
	command=stats.cap+stats.start_time
	execute=os.popen(command).read()
        print(Fore.RED+execute+Style.RESET_ALL)
#Finding the End time of the Capture
def capend():
        command=stats.cap+stats.end_time
        execute=os.popen(command).read()
        print(Fore.GREEN+execute+Style.RESET_ALL)
def capdur():
        command=stats.cap+stats.duration
        execute=os.popen(command).read()
        print(Fore.BLUE+execute+Style.RESET_ALL)	

def capnna():
	command=stats.nna
	execute=os.popen(command).read()
	line=execute.split("\n")
        j=len(line)
        j=j-2
        while(j>=0):
                k=line[j]
                source,mac=k.split(",")
                print"MAC"+"\t\t\t\t\t\t"+"NAME"
		print"==="+"\t\t\t\t\t\t"+"===="
                print Fore.GREEN
                print source+"\t\t\t\t"+mac
                print Style.RESET_ALL
                j=j-1

	
