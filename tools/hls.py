#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
#cPath = os.getcwd()

# 如果目录名字为中文 需要转码处理
#uPath = unicode(cPath,'utf-8')

# 打开文件
path = sys.argv[1]
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
   name,ext = os.path.splitext(file)
   if not os.path.isdir(path+"/"+file) and file.endswith("mp4"):
       print("==="+file+"===")
       name,ext = os.path.splitext(file)
       cmdline = "ffmpeg -i \"{}{}\" -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls \"{}hls/{}.m3u8\"".format(
       path, file, path, name)
       print(cmdline)
       os.system(cmdline)

