#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()                  	
#Show All Successful Authentication Response Module
def show_all_association_response():
        command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.success_auth + notation.sort_auth
        execute=os.popen(command).read()
        source,dest=execute.split(",")
        print"Source"+"\t\t\t\t\t\t"+"Destination"
        print source+"\t\t====>\t\t"+dest


	




	
