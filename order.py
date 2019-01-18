# -*- coding: utf-8 -*-

import os

path = "."

# Return the list of directories
def get_list_of_dir():
    list_of_dir = []
    for dir in os.listdir(path):
        if os.path.isdir(dir):
            list_of_dir.append(dir)          # Only print directories
    return list_of_dir

def order():
    list_of_dir = get_list_of_dir()
    total = len(list_of_dir)
    index = 1
    for dir in list_of_dir:
        if index < 9:
            dest = '0' + str(index) + '.' + dir
        else:
            dest = str(index) + '.' + dir
        index += 1
        os.rename(dir,dest)

order()
print("Congratulations! Remaning fished!")
            
        
        
    

    
                                 
                
