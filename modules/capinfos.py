#!/usr/bin/env python
#
#            --------------------------------------------------
#                            Wireless Forensics Framework
#            --------------------------------------------------
#        Copyright (C) <2014>  <Ap3x Pr3Dat0r (Nipun Jaswal)>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License
#
#    WFF is Wireless Forensics Framework Developed For Penetration Testing and Forensics of Wireless Networks
#
#
#    About Author :
#
#    Founder :Ap3x Pr3Dat0r (Nipun Jaswal)
#    Location : India
#    Email : mail@nipunjaswal.info
#    Blog : www.nipunjaswal.com, www.nipunjaswal.info
################################################################################################################
# Calling Statitistics Modules
from core.forensiclib import capinfos
def menu_capinfo():
	option=raw_input('Wff:Forensic:Stats>')
        if option=="help" or option=="h":
                print("MAC SPOOF CHECK    Short Hand      Fake MAC Check Options Menu                     ")
                print("================   ==========      =============================                   ")
                print("capst                   cs         Show Capture Start Time                         ")
                print("capen                   ce         Show Capture End Time                           ")
		print("capdur                  cd         Show Capture Duration                           ")
                print("go back                 gb         Previous Menu                                   ")
		menu_capinfo()
        elif option=="capst" or option=="cs":
                capinfos.capstart()
                menu_capinfo()
	elif option=="capen" or option=="ce":
                capinfos.capend()
                menu_capinfo()
	elif option=="capdur" or option=="cd":
		capinfos.capdur()
		menu_capinfo()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_capinfo()
	
