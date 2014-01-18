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
def show_all_destination():
	command=notation.libc+ " -r "+notation.pack_file+notation.sortd
	execute=os.popen(command).read()
	line= []
	line=execute.split("\n")
	j=len(line)
	j=j-2
	print("Destination MAC Details")
	print("=======================\n")
	while(j>0):
		url="http://www.macvendorlookup.com/api/BOKEvPx/"+line[j]
		response = urllib.urlopen(url)
		html = response.read()
		addr=html
		if(addr=="none"):
			bd=line[j]
			if(bd=="ff:ff:ff:ff:ff:ff"):
				print(Fore.GREEN)
                       		print("MAC ID:")
                        	print(line[j])
				print("Vendor Details And Address:")
				print("BroadCast Address")
				print(Style.RESET_ALL)
			else:
				print(Fore.RED)
                                print("MAC ID:")
                                print(line[j])
				print("Vendor Details And Address:")
				print("Suspicious")
				print(Style.RESET_ALL)
		else:
			print(Fore.GREEN)
			print("MAC ID:")
			print(line[j])
			print("Vendor Details And Address:")
			print(addr)
			print(Style.RESET_ALL)
		j=j-1

def show_all_source():
	command=notation.libc+ " -r "+notation.pack_file+notation.sorts
	execute=os.popen(command).read()
	line= []
        line=execute.split("\n")
        j=len(line)
        j=j-2
        print("Source MAC Details")
        print("=======================\n")
        while(j>0):
                url="http://www.macvendorlookup.com/api/BOKEvPx/"+line[j]
                response = urllib.urlopen(url)
                html = response.read()
                addr=html
                if(addr=="none"):
                        bd=line[j]
                        if(bd=="ff:ff:ff:ff:ff:ff"):
                                print(Fore.GREEN)
                                print("MAC ID:")
                                print(line[j])
                                print("Vendor Details And Address:")
                                print("BroadCast Address")
                                print(Style.RESET_ALL)
                        else:
                                print(Fore.RED)
                                print("MAC ID:")
                                print(line[j])
                                print("Vendor Details And Address:")
                                print("Suspicious")
                                print(Style.RESET_ALL)
                else:
                        print(Fore.GREEN)
                        print("MAC ID:")
                        print(line[j])
                        print("Vendor Details And Address:")
                        print(addr)
                        print(Style.RESET_ALL)
                j=j-1


	




	
