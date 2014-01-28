#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info

import colorama
from colorama import Fore, Back, Style
colorama.init()
def style():
	Name=   "#Wireless Forensics Framework 0.1v#"
	Author= "#  Developer: Nipun Jaswal(Ap3x)  #"
	print(Fore.RED+"\\\              //===== ||=======   ")
	print(Fore.RED+" \\\            //       ||        ")
	print(Fore.RED+"  \\\   //\\\   //======= ||=======  ")
	print(Fore.RED+"   \\\ //  \\\ //         ||       ")
	print(Fore.RED+"    \\\/    \\//          ||       ")
	print (Back.BLACK + Name + Style.RESET_ALL)
	print (Back.BLACK + Author + Style.RESET_ALL)
	
def help():
	print("Commands\t\t\t\tUsage")
	print("========\t\t\t\t=====")
	print Fore.GREEN+"(h)"+Style.RESET_ALL+"elp\t\t\t\t\tDisplay This Menu"
	print Fore.RED+"(f)"+Style.RESET_ALL+"orensics\t\t\t\tForensics Modules"
	print Fore.CYAN+"(au)"+Style.RESET_ALL+"thor\t\t\t\tAuthor Info"
	print Fore.BLUE+"(e)"+Style.RESET_ALL+"xit\t\t\t\t\tExit WFF"
	print("\n")

