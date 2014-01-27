
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
pack_file="/root/hax.cap"	
#===========================================
#Filter Variables Mgmt Frames
success_auth=""" "wlan.fc.type_subtype==0x0B && wlan_mgt.fixed.auth_seq == 0x0002 && wlan_mgt.fixed.status_code==0x0000" """
associations_req="wlan.fc.type_subtype==0x00"
deauth="wlan.fc.type_subtype==0x0C"
recon_packet=""" "wlan.fc.type_subtype==0x00||wlan.fc.type_subtype==0x01||wlan.fc.type_subtype==0x04||wlan.fc.type_subtype==0x05||wlan.fc.type_subtype==0x08" """
auth_deauth=""" "wlan.fc.type_subtype==0x0B || wlan.fc.type_subtype==0x0C" """
#==========================================
#Filter Variables Data Frames
data="wlan.fc.type==2"
#===========================================
#Sorting and Unique Functions
sorts=" -T fields -e wlan.sa | sort | uniq"
sortd=" -T fields -e wlan.da | sort | uniq"
sort_auth_deauth=" -T fields -E separator=, -e wlan.sa -e wlan.da -e wlan.fc.type_subtype -e frame.number -e frame.time | tr -s ' ' ','"
sort_auth=" -T fields -E separator=, -e wlan.sa -e wlan.da -e frame.time| tr -s ' ' ','"
sort_source_dest=" -T fields -E separator=, -e wlan.sa -e wlan.da | sort| uniq"
sort_deauth=" -T fields -E separator=, -e wlan.sa -e wlan.da| sort | uniq -c | tr -s ' ' ',' | sed 's/^,*//g'"
sort_data_count=" -T fields -E separator=, wlan.sa -e wlan.da -e | sort | uniq -c | tr -s ' ' ',' | sed 's/,//'"
sort_recon=" -T fields -E separator=, -e frame.number -e wlan.fc.type_subtype -e wlan.sa -e wlan.da -e frame.time| tr -s ' ' ','"
frame=" -T fields -e wlan_mgt.fixed.reason_code | tr -s ' ' ','"
#===========================================


