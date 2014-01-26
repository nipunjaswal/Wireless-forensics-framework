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
from core.forensiclib import deauthlib
import colorama
from colorama import Fore, Back, Style
colorama.init()
def menu_deauth():
	option=raw_input('Wff:'+Fore.RED+'Forensic'+Style.RESET_ALL+':'+Fore.GREEN+'DeAuth'+Style.RESET_ALL+'>')
        if option=="help" or option=="h":
                print("General Command\t\t\t\tUsage Information                               ")
                print("===============\t\t\t\t=================                               ")
		print Fore.GREEN+"(sh)ow (t)rans\t\t\t\tShow Clients Sending DeAuth Packets"+Style.RESET_ALL
		print Fore.GREEN+"(g)o back\t\t\t\tPrevious Menu"+Style.RESET_ALL
 		menu_deauth()
        elif option=="show trans" or option=="sht":
                deauthlib.show_all_Deauth()
                menu_deauth()
	elif option=="go back" or option=="gb":
		return
	else:
		menu_deauth()

	
