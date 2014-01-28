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
import colorama
from colorama import Fore, Back, Style
colorama.init()
def menu_fakemac():
        option=raw_input('Wff:'+Fore.RED+'Forensic'+Style.RESET_ALL+':'+Fore.CYAN+'FakeMAC'+Style.RESET_ALL+'>')
        if option=="help" or option=="h":
                print "MAC SPOOF CHECK\t\t\t\tFake MAC Check Options Menu"
                print "================\t\t\t==========================="
                print Fore.CYAN+"(s)how (d)est (m)ac\t\t\tShow All Destinations With Fake MAC Detect"
                print "(s)how (s)ourc (m)ac\t\t\tShow All Sources With Fake MAC Detect"
		print "(g)o (b)ack\t\t\t\tPrevious Menu"+Style.RESET_ALL
                menu_fakemac()
        elif option=="show dest mac" or option=="sdm":
                fakemaclib.show_all_destination()
                menu_fakemac()
	elif option=="show sourc mac" or option=="ssm":
                fakemaclib.show_all_source()
                menu_fakemac()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_fakemac()

