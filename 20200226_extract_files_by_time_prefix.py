#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author bendell02
@desc extract files by time_prefix
@date 20200226
"""

import os
import os.path
import shutil
import datetime
import re
from enum import Enum
import random


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

def get_all_files_name(directory, filename_tuples):
    files = os.listdir(directory)
    for filename in files:
        full_path = os.path.join(directory, filename)
        if os.path.isdir(full_path):
            sud_directory = full_path
            get_all_files_name(sud_directory, filename_tuples)
        elif has_time_prefix(filename) :
            filename_tuples.append((filename, os.path.join(directory, filename)))
        else:
            print filename + ' is invalid.'

def is_file_ok(filename, min_time, max_time):
    current_time = filename[0:8]
    if(current_time>=min_time and current_time<=max_time):
        return True
    
    return False

def make_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        print 'delete ' + folder_name
    os.makedirs(folder_name)
    print 'make dir ' + folder_name

def copy_file(file_name, folder_name):
    if os.path.exists(file_name):
        shutil.copy(file_name, folder_name)
        print 'copy file '+ file_name + ' to ' + folder_name + ' succeed'
    else:
        print '**** error **** copy file '+file_name+' failed'

class Mode(Enum): 
    ONE_WEEK            = 1 # one week;
    TWO_WEEKS           = 2 # two weeks;
    ONE_MONTH           = 3 # one month;
    FIELS_30            = 4 # get 30 files 
    FIELS_30_RANDOMLY   = 5 # get 50 files randomly


def main():
    mode = Mode.TWO_WEEKS
    # mode = Mode.FIELS_30_RANDOMLY

    min_time = ( datetime.date.today() + datetime.timedelta(weeks=-2) ).strftime("%Y%m%d")
    max_time = datetime.datetime.now().strftime("%Y%m%d")    # today
    number_limit = 200
    operation_path = r'E:\61_photo\81_video_small'

    # analysis mode
    if (Mode.ONE_WEEK == mode) :
        min_time = ( datetime.date.today() + datetime.timedelta(weeks=-1) ).strftime("%Y%m%d")
    elif (Mode.TWO_WEEKS == mode) :
        min_time = ( datetime.date.today() + datetime.timedelta(weeks=-2) ).strftime("%Y%m%d") 
    elif (Mode.ONE_MONTH == mode) :
        min_time = ( datetime.date.today() + datetime.timedelta(weeks=-4) ).strftime("%Y%m%d") 
    elif (Mode.FIELS_30 == mode or Mode.FIELS_30_RANDOMLY == mode) :
        min_time = '00000000' 
        number_limit = 30
    else :
        pass

    # make destination folder
    dst_folder_name = min_time + "_" + max_time + "_" + str(mode)[5:]
    make_folder(dst_folder_name)

    # get all filenames
    filename_tuples = [] # (filename, full_path)
    get_all_files_name(operation_path, filename_tuples)

    # sort. descending order
    filename_tuples = sorted(filename_tuples, key=lambda filename_tuple: str(filename_tuple[0]), reverse=True)
    
    # shuffle if in random mode
    if(Mode.FIELS_30_RANDOMLY == mode):
        random.shuffle (filename_tuples)

    # current file
    current_file_name =  os.path.basename(__file__)

    print "\n\n"
    num = 0
    for filename_tuple in filename_tuples:
        if str(current_file_name) == str(filename_tuple[0]):
            continue
        
        if is_file_ok(filename_tuple[0], min_time, max_time):
            copy_file(filename_tuple[1], dst_folder_name)
        else:
            print '\nbeyond time section\n'
            break

        num += 1
        if(num >= number_limit):
            print '\nbeyond number limit(' + str(number_limit) + ')...\n'
            break
        
    print '\ntotal %d files\n' % (num)
    raw_input('end')


if __name__=='__main__':
    main()