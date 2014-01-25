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
	print("Commands\t\tUsage")
	print("========\t\t=====")
	print Fore.RED+"(h)"+Style.RESET_ALL+"elp\t\t\tDisplay This Menu"
	print Fore.RED+"(a)"+Style.RESET_ALL+"ttacks\t\tAttack Modules"
	print Fore.RED+"(f)"+Style.RESET_ALL+"orensics\t\tForensics Modules"
	print Fore.RED+"(au)"+Style.RESET_ALL+"thor\t\tAuthor Info"
	print Fore.RED+"(e)"+Style.RESET_ALL+"xit\t\t\tExit WFF"
	print("\n")

