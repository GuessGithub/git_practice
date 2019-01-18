# -*- coding: utf-8 -*-

import os

path = "."

def change(which):
    for dir in os.listdir(path):
        # Handle only with directory!
        if os.path.isdir(dir):
            str0 = dir.split(".",1)[0]
            if str0.isdigit():
                int0 = int(str0)
                if int0 < which:
                    continue
                if int0 >= which:
                    int0 = int0 + 1
                    if int0 >= 10:
                        str0 = str(int0)
                    else:
                        str0 = str(int0)
                        str0 = '0' + str0
                    dest = str0 + "." + dir.split(".",1)[1]
            else:
                if which < 10:
                    str_which = "0" + str(which)
                else:
                    str_which = str(which)
                dest = str_which + "." + dir
            os.rename(dir,dest)

change(2)
    
                                 
                
