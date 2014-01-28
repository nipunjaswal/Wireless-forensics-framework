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
from core.forensiclib import reconlib
def menu_recon():
        option=raw_input('Wff:Forensic:Recon>')
        if option=="help" or option=="h":
                print "General Command\t\t\t\tUsage Information"
                print "===============\t\t\t\t================="
                print "(r)un\t\t\t\t\tShow All Successful Authentications"
                print "(g)o (b)ack\t\t\t\tPrevious Menu"
                menu_recon()
        elif option=="run" or option=="r":
                reconlib.runmod()
                menu_recon()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_recon()

	
