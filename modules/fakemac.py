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
from core.forensiclib import fakemaclib
def menu_fakemac():
        option=raw_input('Wff:Forensic:FakeMac>')
        if option=="help" or option=="h":
                print("MAC SPOOF CHECK    Short Hand      Fake MAC Check Options Menu                     ")
                print("================   ==========      =============================                   ")
                print("show dest mac           sd         Show All Destinations With Fake MAC Detect      ")
                print("show sourc mac          ss         Show All Sources With Fake MAC Detect           ")
		print("go back                 gb         Previous Menu                                   ")
                menu_fakemac()
        elif option=="show dest mac" or option=="sd":
                fakemaclib.show_all_destination()
                menu_fakemac()
	elif option=="show sourc mac" or option=="ss":
                fakemaclib.show_all_source()
                menu_fakemac()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_fakemac()

