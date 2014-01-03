#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
import os
import sys
from modules import show_destinations 
def forensic_menu():
	option=raw_input('Wff:Forensic>')
	if option=="help" or option=="h":
		print("Command	  Short Hand      Usage                 ")
		print("========   ==========      =====                 ")
		print("help            h          Display This Menu     ")
		print("show dest       sd         Show All Destinations ")
		print("exit            e          Exit WFF              ")
		print("\n")
		forensic_menu()
	elif option=="show dest" or option=="sd":
		show_destinations.show_dest()
		forensic_menu()
	elif option=="exit" or option=="e":
		sys.exit(0)
	else:
		forensic_menu()
	return
		

