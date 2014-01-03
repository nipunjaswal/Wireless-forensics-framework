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
from conf import notation
def set_path():
	new_path=raw_input("Enter New File Path (Ex- /abc/adc-01.cap):")
	notation.pack_file=new_path
def show_path():
	print "Current File:"
	print notation.pack_file		

	
