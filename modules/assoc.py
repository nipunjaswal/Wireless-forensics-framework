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
from core.forensiclib import assoclib
def menu_assoc():
        option=raw_input('Wff:Forensic:Assoc>')
        if option=="help" or option=="h":
                print("General Command     Short Hand      Usage Information                               ")
                print("===============    ==========      =================                               ")
                print("show assoc            sa          Show All Transmissions                          ")
                print("go back               gb           Previous Menu                                   ")
                menu_assoc()
        elif option=="show assoc" or option=="sa":
                assoclib.show_all_association_requests()
                menu_assoc()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_assoc()

	
