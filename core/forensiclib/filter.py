#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
def show_all_destination():
	this_file=file
	command=notation.libc+ " -r "+notation.pack_file+" -T fields -e wlan.da | sort | uniq"
	execute=os.system(command)
	print(execute)


