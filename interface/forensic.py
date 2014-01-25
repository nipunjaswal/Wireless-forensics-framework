#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
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
	option=raw_input('Wff:Forensic>')
	if option=="help" or option=="h":
		print("GENERAL COMMANDS	   Short Hand     Usage Information                               ")
		print("================    ==========     =================                               ")
		print("Stats                   s          Display Time,Duration Etc.                      ")
		print("help                    h          Display This Menu                               ")
		print("go back                 gb         Previous Menu                                   ")
		print("exit                    e          Exit WFF                                        ")
		print("\n")
		print("\n")
		print("SUB MENU           Short Hand      Complex Mgmt Frame Operations                   ")
		print("========           ==========      =============================                   ")
		print("Assoc                   A          Association Operations Menu                     ")
		print("DeAuth                  D          Deauth Operations Menu                          ")
		print("FakeMac                 F          Fake MAC Detection Menu                         ")
		print("Data                    DT         Data Operations Menu                            ")
		print("AuTh                    AT         Authentication Operations Menu                  ")
		print("ReCon                   R          Reconstruct The Crime Scene                     ")
		print("\n")
		print("File Options       Short Hand      Usage Information                               ")
		print("============       ==========      =================                               ")
		print("set file                sf         Set File                                        ")
		print("show file               shf        Show File                                       ")
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
		return
	elif option=="exit" or option=="e":
		sys.exit(0)
	else:
		forensic_menu()
	return
		

