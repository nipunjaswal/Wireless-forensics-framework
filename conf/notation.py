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
#Filter Variables Mgmt Frames
success_auth="wlan.fc.type_subtype==0x0B && wlan_mgt.fixed.auth_seq == 0x0002 && wlan_mgt.fixed.status_code==0x0000)"
associations_req="wlan.fc.type_subtype==0x00"
deauth="wlan.fc.type_subtype==0x0C"
#==========================================
#Filter Variables Data Frames
data="wlan.fc.type==2"
#===========================================
#Sorting and Unique Functions
sorts=" -T fields -e wlan.sa | sort | uniq"
sortd=" -T fields -e wlan.da | sort | uniq"
sort_auth=" -T fields -E separator=, -e wlan.sa -e wlan.da -e frame.time| tr -s ' ' ','"
sort_source_dest=" -T fields -E separator=, -e wlan.sa -e wlan.da | sort| uniq"
sort_data_count=" -T fields -E separator=, wlan.sa -e wlan.da -e |sort | uniq -c | tr -s ' ' ',' | sed 's/,//'"
#===========================================

