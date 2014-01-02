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
from core.forensiclib import filter
def show_dest():
	x=raw_input("Enter File Path(Ex- ~/abc.cap)")
	filter.show_all_destination(x)
