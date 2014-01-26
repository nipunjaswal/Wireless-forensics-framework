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
from core.forensiclib import authlib
def menu_auth():
        option=raw_input('Wff:Forensic:AuTh>')
        if option=="help" or option=="h":
                print("General Command     Short Hand      Usage Information                               ")
                print("===============    ==========      =================                               ")
                print("show sauth            st           Show Authentications Requests                   ")
                print("go back               gb           Previous Menu                                   ")
                menu_auth()
        elif option=="show sauth" or option=="st":
                authlib.show_all_association_response()
                menu_auth()
        elif option=="go back" or option=="gb":
                return
        else:
                menu_auth()

	
