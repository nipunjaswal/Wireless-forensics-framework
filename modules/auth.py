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
import colorama
from colorama import Fore, Back, Style
colorama.init()
from core.forensiclib import authlib
def menu_auth():
        option=raw_input('Wff:'+Fore.RED+'Forensic'+Style.RESET_ALL+':'+Fore.MAGENTA+'AuTh'+Style.RESET_ALL+'>')
        if option=="help" or option=="h":
                print "General Command\t\t\t\tUsage Information"
                print "===============\t\t\t\t================="
                print Fore.MAGENTA+"(s)how (sa)uth\t\t\t\tShow Authentications Requests"
		print "(s)how (f)ailed\t\t\t\tShow Failed Authentication Tries"
                print "(g)o (b)ack\t\t\t\tPrevious Menu"+Style.RESET_ALL
                menu_auth()
        elif option=="show sauth" or option=="ssa":
                authlib.show_all_association_response()
                menu_auth()
	elif option=="show failed" or option=="sf":
		authlib.show_failed_attempts()
		menu_auth()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_auth()

	
