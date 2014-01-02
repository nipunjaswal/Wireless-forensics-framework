#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info

import colorama
from colorama import Fore, Back, Style
colorama.init()
def style():
	Name=  "#         Wireless Forensics Framework 0.1v       #"
	Author=  "#          Developer : Nipun Jaswal(Ap3x)         #"
	print  "###################################################"
	print  "###################################################"
	print  "###################################################"
	print (Back.RED + Name + Style.RESET_ALL)
	print (Back.RED + Author + Style.RESET_ALL)
	print  "###################################################"
	print  "###################################################"
	print  "###################################################"
	
def help():
	print("Commands         Usage            ")
	print("========         =====            ")
	print("help             Display This Menu")
	print("attacks          Attack Modules   ")
	print("forensics        Forensics Modules")
	print("Author           Author Info      ")
	print("\n")

