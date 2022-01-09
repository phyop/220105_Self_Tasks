#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# -*- coding: utf-8 -*-
import re

file_name_in = input('file name without .txt: ')
path_in = './' + file_name_in + '.txt'
path_out = './'+ file_name_in + '_out' +'.txt'
print('path_in: ', path_in)
print('path_out: ', path_out)

f_in = open(path_in,'r',encoding="utf-8")
f_out = open(path_out,'w',encoding="utf-8")
lines = f_in.readlines()
for line in lines:
    line = line.strip()
    line = re.sub('^\d+', '', line)
    line = line.strip()
    f_out.writelines(line+"\n")
    # . 單一字元   ？ 0或1次   * 0~多次   + 1~多次   .* 任意字元 0~多次
f_in.close()
f_out.close()
    

"""
# https://reurl.cc/venZ3a
f = open("a.txt")
f.read() 
# 從檔案當前位置起讀取size個位元組，若無引數size，則表示讀取至檔案結束為止，它範圍為字串物件
# 如果檔案大於可用記憶體，不可能使用這種處理
f.readline()
# 每次讀出一行內容，所以，讀取時佔用記憶體小，比較適合大檔案，該方法返回一個字串物件
# 1、readline()每次讀取一行，比readlines()慢得多
# 2、readline()返回的是一個字串物件，儲存當前行的內容
f.readlines()
# readlines()方法讀取整個檔案所有行，儲存在一個列表(list)變數中，每行作為一個元素，但讀取大檔案會比較佔記憶體。
linecache.getline('a.txt',2) # 輸出第2行



# https://reurl.cc/Mb7amL
*:前面的字元可出現零次以上
+:前面的字元至少要出現一次以上
{m,n}:前面的字元可出現m次~n次(包含)
[0-9]:0~9之間的任意數字
[a-z]:a~z之間的任意文字(小寫)
[A-Z]:A~Z之間的任意文字(大寫)
.:代表任何字元(符號、數字、空格)
\:跳脫字元  例如:\+(尋找+號)
|:代表"或"(符合其中一個即可)
\w:代表任何字母或數字，等同於[a-z A-Z 0-9]
\d:代表匹配十進位數字，即[0-9]

print(result.group())   #group方法可以輸出所有匹配的內容
print(result.group(1))  #group(1)輸出第1個匹配的內容,也可輸出第2、第3

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
#回傳None(因為match從開頭進行比對)
result = re.match('Hello.*?(\d+).*?Demo', content)
#回傳出數值(使用search方法，整串搜尋)
result = re.search('Hello.*?(\d+).*?Demo', content)

import re
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content) 
#第一個參數是要取代的,第二個參數是想變成的
#第二個參數若為空，則可以變成取代功能
#第三個參數為原本的字串
print(content) #印出的結果無任何數字存在
"""

"""
https://www.itread01.com/article/1521463875.html
程式碼一
if line.split():
    outfopen.writelines(line)
else:
    outfopen.writelines("")
程式碼二
line = line.strip()
    if len(line)!=0:
        outfopen.writelines(line)
        outfopen.write('\n')
1. Python split()通過指定分隔符對字串進行切片,返回分割後的字串列表。str.split()分隔符預設為空格。
2. 函式 writelines(list）
    函式writelines可以將list寫入到檔案中，但是不會在list每個元素後加換行符，所以如果想每行都有換行符的話需要自己再加上。
    例如：for line in lines:
        outfopen.writelines(line+"\n")
"""

"""
https://blog.csdn.net/Zhongjie1986/article/details/91448373
file.write(str)的参数是一个字符串，就是你要写入文件的内容.
file.writelines(sequence)的参数是序列，比如列表，它会迭代帮你写入文件。
file.writelines(['love\n','python\n','love python\n']) 
writelines()函数的参数也可以是一个字符串，用法跟write()函数类似。
file.writelines('love\npython\nlove python\n')
"""

# ls -l@看一下有哪些隐藏属性
# sudo xattr -r -d com.apple.quarantine +目录路径

# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
# -*- coding: utf-8 -*-
# 或者 # coding=utf-8 就行了
# 注意： # coding=utf-8 的 = 号两边不要空格。
