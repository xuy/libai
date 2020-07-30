#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open("libai.txt", "r")
l = f.next()
try:
  while True:
    # seek subject
    while len(l) < 2 or "。" in l or l.startswith("(") or ")" in l or " " in l or '-' in l:
      l = f.next()
    print "\n\t标题: ", l, 
    while "。" not in l:
      l = f.next()
    # body
    print "\t句头: ",
    header = []
    while "。" in l:
      k = unicode(l.decode('utf-8'))
      header.append(k[0]) 
      l = f.next()
    print ''.join(header)

except StopIteration:
  f.close()