#!/usr/bin/python
# -*- coding: utf-8 -*- 

import win32gui
import os
import os.path
import shutil

SW_HIDE = 0
SW_SHOW = 5
SW_MINIMIZE = 6
SW_SHOWMINNOACTIVE = 7
file_name = '_ReadMe.txt'
template_file = 'D:\\91_tools\\_ReadMe_template.txt'


def enumerationCallaback(hwnd, results):
    className = win32gui.GetClassName(hwnd)
    text = win32gui.GetWindowText(hwnd)
    if(className == 'ToolbarWindow32'):
        # change pattern if in no-chinese system
        pattern = '地址: '.decode('utf-8').encode('gb2312') 
        if(text.find(pattern) >= 0):
            results.append(text[6:])


def get_path(path):
    for i in range(500):
    # while True:
        window = win32gui.GetForegroundWindow()
        if (window != 0):                
            if (win32gui.GetClassName(window) == 'CabinetWClass'):
                win32gui.EnumChildWindows(window, enumerationCallaback, path)
                break
            else:
                if (win32gui.GetClassName(window) == 'ConsoleWindowClass'):
                    win32gui.ShowWindow(window, SW_MINIMIZE)

def main():
    path = []
    get_path(path)

    if path:
        if os.path.exists(path[0]):
            fileName_with_full_path = os.path.join(path[0], file_name)
            if not os.path.exists(fileName_with_full_path):
                shutil.copyfile(template_file, fileName_with_full_path)
                print('create file '+fileName_with_full_path)
            else:
                print(fileName_with_full_path+' is already exists')
        else:
            print('***error:*** the path is not exists')
    else:
        print('***error:*** the path is empty')

    # raw_input()



if __name__=='__main__':
    main()
