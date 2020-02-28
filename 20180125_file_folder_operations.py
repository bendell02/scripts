#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil

def copy_file(file_name, folder_name):
    if os.path.exists(file_name):
        shutil.copy(file_name, folder_name)
        print 'copy '+ file_name + ' to ' + folder_name + ' succeed'
    else:
        print '**** error **** copy file '+file_name+' failed'

def copy_folder(folder_before, folder_after):
    if os.path.exists(folder_before):
        shutil.copytree(folder_before, folder_after)
        print 'copy ' + folder_before + ' to ' + folder_after + ' succeed'
    else:
        print '**** error **** copy folder '+folder_before+' failed'

def make_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        print 'delete ' + folder_name
    os.makedirs(folder_name)
    print 'make dir ' + folder_name

def delete_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        print 'delete ' + folder_name
    else:
        print folder_name + ' does not exist, no need to delete'