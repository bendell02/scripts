#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import os.path
import shutil
import time
import re


def has_time_prefix(name):
    # OK example 20200226_xxxx
    # length 
    if(len(name) <= 9):
        return False

    # number and _
    res = re.match(r'\d{8}_', name[0:9])
    if(not res):
        return False

    return True

def main():
    current_path = os.getcwd()
    files = os.listdir(current_path)
    current_file_name =  os.path.basename(__file__)
    time_prefix = time.strftime("%Y%m%d", time.localtime())
    
    filenames_before_rename = []
    filenames_after_rename = []
    has_file_changed = False

    for filename in files:
        if has_time_prefix(filename):
            continue

        if not os.path.isdir(filename) and filename != current_file_name:

            filename_after = "%s_%s" % (time_prefix, filename)
            os.rename(filename, filename_after)

            filenames_before_rename.append(filename)
            filenames_after_rename.append(filename_after)
            print filename + '  convert to  ' + filename_after
            has_file_changed = True
    
    if has_file_changed:
        is_ok = raw_input("is it ok? n/Y:")
    else:
        is_ok = ""
        print 'no file changed'

    if(is_ok in (["N", 'n', 'No', 'NO', 'nO', 'no'])):
        for i in range(len(filenames_before_rename)):
            os.rename(filenames_after_rename[i], filenames_before_rename[i])            
            print filenames_after_rename[i] + '  invert to  ' + filenames_before_rename[i]
			
    raw_input('end')


if __name__=='__main__':
    main()
    