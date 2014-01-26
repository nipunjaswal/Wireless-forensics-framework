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
from core.forensiclib import assoclib
def menu_assoc():
        option=raw_input('Wff:'+Fore.RED+'Forensic'+Style.RESET_ALL+':'+Fore.YELLOW+'Assoc'+Style.RESET_ALL+'>')
        if option=="help" or option=="h":
                print("General Command\t\t\t\tUsage Information")
                print("===============\t\t\t\t=================")
                print Fore.YELLOW+"(s)"+Style.RESET_ALL+"how "+Fore.YELLOW+"(a)"+Style.RESET_ALL+"ssoc\t\t\t\tShow All Transmissions"
                print Fore.YELLOW+"(g)"+Style.RESET_ALL+"o "+Fore.YELLOW+"(b)"+Style.RESET_ALL+"ack\t\t\t\tPrevious Menu"
                menu_assoc()
        elif option=="show assoc" or option=="sa":
                assoclib.show_all_association_requests()
                menu_assoc()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_assoc()

	
