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
    if check_begin_with_digit(list_dir):
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
    else:
        print("Sorry, you can reorder only if there is only one dir whose prefix is not pure digits.")

def check_begin_with_digit(list_checked):
    mark = 0
    for dir in list_checked:
        if not dir.split(".",1)[0].isdigit():
            mark += 1
    if mark == 1:
        return True
    else:
        return False
            


# Make suer that an integer has been input.
while True:
    str_pos = input("input:")
    if str_pos.isdigit():
        break
    print("You just input " + str_pos + " ! Please input an integer!")
int_pos = int(str_pos)           
add_new_dir_remain_ordered(int_pos)
                                 
                
