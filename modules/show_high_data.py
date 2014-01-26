
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
from core.forensiclib import datalib
import colorama
from colorama import Fore, Back, Style
colorama.init()
def menu_show_high_data():
	option=raw_input('Wff:'+Fore.RED+'Forensic'+Style.RESET_ALL+':'+Fore.BLUE+'Data'+Style.RESET_ALL+'>')
        if option=="help" or option=="h":
                print "MAC SPOOF CHECK\t\t\t\tFake MAC Check Options Menu"
                print "================\t\t\t============================="
                print Fore.BLUE+"(s)how (d)a(t)a\t\t\t\tShow All Destinations With Fake MAC Detect"
		print "(g)o (b)ack\t\t\t\tPrevious Menu"+Style.RESET_ALL
                menu_show_high_data()
	elif option=="show data" or option=="sdt":
                datalib.show_high_data()
                menu_show_high_data()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_show_high_data()
	
