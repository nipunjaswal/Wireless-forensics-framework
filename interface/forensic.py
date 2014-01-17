#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
import os
import sys
from modules import show_deauth
from modules import show_destinations
from modules import show_associations
from modules import show_sources
from modules import set_file_path 
def forensic_menu():
	option=raw_input('Wff:Forensic>')
	if option=="help" or option=="h":
		print("General Command	  Short Hand      Usage Information                               ")
		print("===============    ==========      =================                               ")
		print("help                    h          Display This Menu                               ")
		print("exit                    e          Exit WFF                                        ")
		print("\n")
		print("Forensic Command   Short Hand      Usage Information                               ")
                print("================   ==========      =================                               ")
		print("show dest               sd         Show All Destinations                           ")
		print("show sourc              ss         Show All Sources                                ")
		print("show assoc              sa         Show All Clients Who Sent Authentication Request")
		print("show deauth             sdd        Show All Deauthentications                      ")
		print("\n")
		print("File Options       Short Hand      Usage Information                               ")
		print("============       ==========      =================                               ")
		print("set file                sf	  Set File                                        ")
		print("show file               shf        Show File                                       ")
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
	elif option=="show assoc" or option=="sa":
		show_associations.show_auth()
		forensic_menu()
	elif option=="show sourc" or option=="ss":
		show_sources.show_source()
		forensic_menu()
	elif option=="show deauth" or option=="sdd":
		show_deauth.show_deauth()
		forensic_menu()
	elif option=="exit" or option=="e":
		sys.exit(0)
	else:
		forensic_menu()
	return
		

