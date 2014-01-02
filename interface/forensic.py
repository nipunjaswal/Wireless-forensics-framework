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
	if option=="help":
		print("Command	        Usage                 ")
		print("========         =====                 ")
		print("help             Display This Menu     ")
		print("show dest        Show All Destinations ")
		print("exit		Exit WFF              ")
		print("\n")
		forensic_menu()
	elif option=="show dest":
		show_destinations.show_dest()
		#calltomain="python wff.py"
		#os.system(calltomain)
	elif option=="exit":
		sys.exit(0)
	else:
		forensic_menu()
	return
		

