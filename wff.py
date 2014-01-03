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
import os
import sys
from interface import intf
from interface import forensic
from core.forensiclib import notation 
intf.style()
def main():
	option=raw_input('Wff>')
	if option=="help" or option=="h":
		intf.help()
		main()
	elif option=="forensics" or option=="f":
		forensic.forensic_menu()
	elif option=="exit" or option=="e":
		sys.exit(0)
	else:
		main()
if __name__ == "__main__":
    main()

