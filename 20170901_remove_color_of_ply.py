#! /usr/bin/env python
# -*- coding: utf-8 -*-

### 用于把点云的颜色去除，只适用于 ascii 形式，不适用于二进制的格式

import os
import re

fileName = raw_input('input name: ')
file_mine = fileName + '.ply'
f_mine = open(file_mine)
content_mine = f_mine.read()
f_mine.close()

re_exp = r'(\s\d+){3}(?=\n)'

try:
    content_mine = re.sub(re_exp, r'', content_mine)
    content_mine = re.sub(r'property uchar red\nproperty uchar green\nproperty uchar blue\n', r'', content_mine)
    content_mine = re.sub(r'element camera 1\nproperty float view_px\nproperty float view_py\nproperty float view_pz\nproperty float x_axisx\nproperty float x_axisy\nproperty float x_axisz\nproperty float y_axisx\nproperty float y_axisy\nproperty float y_axisz\nproperty float z_axisx\nproperty float z_axisy\nproperty float z_axisz\nproperty float focal\nproperty float scalex\nproperty float scaley\nproperty float centerx\nproperty float centery\nproperty int viewportx\nproperty int viewporty\nproperty float k1\nproperty float k2', r'element face 0\nproperty list uchar int vertex_indices', content_mine)
    content_mine = re.sub(r'(\s\d+){7,}(?=\n)', r'', content_mine)
except:
    print "..........error....."
    
fileName = fileName + '_after.ply'

f = open(fileName, 'w')
f.write(content_mine)
f.close()


raw_input('end')

