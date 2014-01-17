#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
import os
#===========================================
#Name of The Packet Filterer
libc="tshark"
#===========================================
#Current File Loaded
pack_file="~/deepak-01.cap"	
#===========================================
#Filter Variables
authentications="wlan.fc.type_subtype==0x0B"
associations_req="wlan.fc.type_subtype==0x00"
deauth="wlan.fc.type_subtype==0x0C"
#===========================================
#Sorting and Unique Functions
sorts=" -T fields -e wlan.sa | sort | uniq"
sortd=" -T fields -e wlan.da | sort | uniq"
sort_source_dest=" -T fields -E separator=, -e wlan.da -e wlan.sa | sort| uniq"
#===========================================
