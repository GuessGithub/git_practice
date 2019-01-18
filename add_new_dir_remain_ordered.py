# -*- coding: utf-8 -*-

import os

path = "."

def get_list_of_dir():
    list_of_dir = []
    for dir in os.listdir(path):
        if os.path.isdir(dir):
            list_of_dir.append(dir)          # Only print directories
    return list_of_dir

def add_new_dir_remain_ordered(pos):
    list_dir = get_list_of_dir()
    print(list_dir)
    for dir in list_dir:
        str0 = dir.split(".",1)[0]
        if str0.isdigit():
            int0 = int(str0)
            if int0 < pos:
                continue
            elif int0 >= pos:
                    int0 = int0 + 1
                    print(int0)
                    if int0 >= 10:
                        str0 = str(int0)
                    else:
                        str0 = str(int0)
                        str0 = '0' + str0
                    dest = str0 + "." + dir.split(".",1)[1]
                    os.rename(dir,dest)
        else:
            if pos < 10:
                str_which = "0" + str(pos)
            else:
                str_which = str(pos)
            dest = str_which + "." + dir
            os.rename(dir,dest)

int_pos = int(input("Please input the position:"))           
add_new_dir_remain_ordered(int_pos)
                                 
                
