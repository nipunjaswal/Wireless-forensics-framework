#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
import os
import sys
from modules import show_destinations
from modules import set_file_path 
def forensic_menu():
	option=raw_input('Wff:Forensic>')
	if option=="help" or option=="h":
		print("Command	          Short Hand      Usage                 ")
		print("========           ==========      =====                 ")
		print("help                    h          Display This Menu     ")
		print("show dest               sd         Show All Destinations ")
		print("exit                    e          Exit WFF              ")
		print("=========================================================")
		print("File Options       Short Hand      Usage                 ")
		print("============       ==========      =====                 ")
		print("set file                sf	  Set File              ")
		print("show file               shf        Show File             ")
		print("\n")
		forensic_menu()
	elif option=="show dest" or option=="sd":
		show_destinations.show_dest()
		forensic_menu()
	elif option=="set file"  or option=="sf":
		set_file_path.set_path()
		forensic_menu()
	elif option=="show file" or option=="shf":
		set_file_path.show_path()
		forensic_menu()
	elif option=="exit" or option=="e":
		sys.exit(0)
	else:
		forensic_menu()
	return
		

