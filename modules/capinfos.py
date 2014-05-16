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
import colorama
from colorama import Fore, Back, Style
colorama.init()
from core.forensiclib import capinfos
def menu_capinfo():
	option=raw_input('Wff:'+Fore.RED+'forensic'+Style.RESET_ALL+':'+Fore.RED+'stats'+Style.RESET_ALL+'>')
        if option=="help" or option=="h":
                print "MAC SPOOF CHECK\t\t\t\tFake MAC Check Options Menu"
                print "================\t\t\t============================="
                print Fore.RED+"(c)ap(s)t\t\t\t\tShow Capture Start Time"
                print "(c)ap(e)n\t\t\t\tShow Capture End Time"
		print "(c)ap(d)ur\t\t\t\tShow Capture Duration"
                print "(n)etwork(n)(a)me\t\t\t\tNetwork Name and Address"
		print "(g)o (b)ack\t\t\t\tPrevious Menu"+Style.RESET_ALL
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
	elif option=="nna":
		capinfos.capnna()
		menu_capinfo()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_capinfo()
	
