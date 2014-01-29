#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
import colorama
from colorama import Fore, Back, Style
colorama.init()
import os
import sys
from modules import show_high_data
from modules import capinfos
from modules import deauth
from modules import assoc
from modules import fakemac
from modules import set_file_path 
from modules import auth
from modules import recon
def forensic_menu():
	option=raw_input('Wff:'+Fore.RED+'Forensic'+Style.RESET_ALL+'>')
	if option=="help" or option=="h":
		print "GENERAL COMMANDS\t\t\tUsage Information"
		print "================\t\t\t================="
		print Fore.RED+"(s)"+Style.RESET_ALL+"tats\t\t\t\t\tDisplay Time,Duration Etc."
		print Fore.GREEN+"(h)"+Style.RESET_ALL+"elp\t\t\t\t\tDisplay This Menu"
		print Fore.BLACK+"(g)"+Style.RESET_ALL+"o "+Fore.BLACK+"(b)"+Style.RESET_ALL+"ack\t\t\t\tPrevious Menu"
		print Fore.BLACK+"(e)"+Style.RESET_ALL+"xit\t\t\t\t\tExit WFF"
		print("\n")
		print "SUB MENU\t\t\t\tComplex Mgmt Frame Operations"
		print "========\t\t\t\t============================="
		print Fore.YELLOW+"(A)"+Style.RESET_ALL+"ssoc\t\t\t\t\tAssociation Operations Menu"
		print Fore.GREEN+"(D)"+Style.RESET_ALL+"eauth\t\t\t\tDeauth Operations Menu"
		print Fore.CYAN+"(F)"+Style.RESET_ALL+"akeMac\t\t\t\tFake MAC Detection Menu"
		print Fore.BLUE+"(D)"+Style.RESET_ALL+"a"+Fore.BLUE+"(T)"+Style.RESET_ALL+"a\t\t\t\tData Operations Menu"
		print Fore.MAGENTA+"(A)"+Style.RESET_ALL+"u"+Fore.MAGENTA+"(T)"+Style.RESET_ALL+"h\t\t\t\tAuthentication Operations Menu"
		print Fore.BLACK+"(R)"+Style.RESET_ALL+"eCon\t\t\t\t\tReconstruct The Crime Scene"
		print("\n")
		print "File Options\t\t\t\tUsage Information"
		print "============\t\t\t\t================="
		print Fore.GREEN+"(s)"+Style.RESET_ALL+"et "+Fore.GREEN+"(f)"+Style.RESET_ALL+"ile\t\t\t\tSet File"
		print Fore.RED+"(sh)"+Style.RESET_ALL+"ow "+Fore.RED+"(f)"+Style.RESET_ALL+"ile\t\t\t\t"+"Show File"
		print("\n")
		forensic_menu()
	elif option=="set file"  or option=="sf":
		set_file_path.set_path()
		forensic_menu()
	elif option=="show file" or option=="shf":
		set_file_path.show_path()
		forensic_menu()
	elif option=="Assoc" or option=="A":
		assoc.menu_assoc()
		forensic_menu()
	elif option=="Data" or option=="DT":
                show_high_data.menu_show_high_data()
                forensic_menu()
	elif option=="stats" or option=="s":
                capinfos.menu_capinfo()
                forensic_menu()
	elif option=="FakeMac" or option=="F":
		fakemac.menu_fakemac()
		forensic_menu()
	elif option=="DeAuth" or option=="D":
		deauth.menu_deauth()
		forensic_menu()
	elif option=="AuTh" or option=="AT":
		auth.menu_auth()
		forensic_menu()
	elif option=="go back" or option=="gb":
		return
	elif option=="ReCon" or option=="R":
		recon.menu_recon()
		forensic_menu()
	elif option=="exit" or option=="e":
		sys.exit(0)
	else:
		forensic_menu()
	return
		

