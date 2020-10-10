#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, sys
import codecs
from xml.sax.saxutils import escape
from pyh import *

reload(sys)
sys.setdefaultencoding('utf-8') 
# 打开文件
path = sys.argv[1]
dirs = os.listdir( path )

title = sys.argv[2]
page = PyH(title)
page.addCSS('../css/common.css')
page.addJS('../js/tools.js')

# 输出所有文件和文件夹
for file in dirs:
   if os.path.isdir(path+"/"+file) and os.path.isdir(path+"/"+file+"/hls"):
      myDiv = div(cl = "box")
      f="urlHtml(\'"+path+"/"+file+"/hls/"+file+".m3u8\')"
      print f
      myA = a(unicode(file),cl = "f40",href = "#",onclick=f)
      myDiv << myA
      page << myDiv
page.body.attributes['bgcolor']="#d0d0a0"
html = page.render()
ofile=path+"/index.html"
o_f = codecs.open(ofile, 'w', encoding= 'utf-8')
o_f.write(html)
o_f.close()
