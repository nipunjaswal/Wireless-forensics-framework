#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
import notation
import os
def show_all_destination(file):
	this_file=file
	command="tshark -r "+this_file+" -T fields -e wlan.da | sort | uniq"
	execute=os.system(command)
	print(execute)


