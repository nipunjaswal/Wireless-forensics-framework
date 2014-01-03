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
	print("Commands   ShortHand         Usage          ")
	print("========   =========         =====          ")
	print("help           h           Display This Menu")
	print("attacks        a           Attack Modules   ")
	print("forensics      f           Forensics Modules")
	print("author         a           Author Info      ")
	print("exit           e           Exit WFF         ")
	print("\n")

