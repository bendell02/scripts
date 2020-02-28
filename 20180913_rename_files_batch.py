#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import shutil
import time

## files no more than 99
## rename file in a format 20180913_basename01.jpg


def main():
    current_path = os.getcwd()
    files = os.listdir(current_path)
    current_file_name =  os.path.basename(__file__)
    time_prefix = time.strftime("%Y%m%d", time.localtime())
    index = 0
    base_name = raw_input('please input the base name')

    for file in files:
        if not os.path.isdir(file) and file != current_file_name:
            file_suffix = os.path.splitext(file)[1]
            file_name_after = "%s_%s%02d%s" % (time_prefix, base_name, index, file_suffix)
            index += 1
            os.rename(file, file_name_after)
            print file + '  convert to  ' + file_name_after
            
            if index>=100:
                print('break!!! The number of files should not be more than 99')
                break
    
    print('Rename %d files totally.' % (index))

if __name__=='__main__':
    main()
    

