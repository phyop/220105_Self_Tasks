#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# -*- coding: utf-8 -*-
import re

count = 0
start = ''

file_name_in = input('file name without .txt: ')
path_in = './' + file_name_in + '.txt'
path_out = './'+ file_name_in + '_out' +'.txt'
print('path_in: ', path_in)
print('path_out: ', path_out)

f_in = open(path_in,'r',encoding="utf-8")
f_out = open(path_out,'w',encoding="utf-8")
lines = f_in.readlines()
for line in lines:
    start = str(count).rjust(4, ' ')
    line = start + ' ' + line
    # line = str(count) + ' ' + line
    f_out.writelines(line)
    count += 1
f_in.close()
f_out.close()

