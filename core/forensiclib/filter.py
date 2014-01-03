#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
pcap_file=notation.pack_file
libcap_var=notation.libc
auth_pack_filter=notation.authentications
sort_source=notation.sorts
sort_dest=notation.sortd
assoc_req=notation.associations_req
sort_source_dest=notation.sort_source_dest
def show_all_destination():
	command=libcap_var+ " -r "+pcap_file+sort_dest
	print("Destinations")
	print("============")
	execute=os.popen(command).read()
	print(execute)
def show_all_source():
	print("Sources")
        print("=======")
	command=libcap_var+ " -r "+pcap_file+sort_source
	execute=os.popen(command).read()
	print(execute)

def show_all_association_requests():
	command=libcap_var+ " -r "+pcap_file+" -R "+assoc_req + sort_source_dest
	execute=os.popen(command).read()
	source,dest=execute.split(",")
	print"Source"+"\t\t\t\t\t\t"+"Destination"
	print source+"\t\t\t\t"+dest
	


	
