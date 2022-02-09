""" 
將 『3,g,6,s,9,n,2,d』的數字及字母區分開來，
分別印出一行數字，一行字母，並用逗號區分」
"""

import string
s = "3,g,6,s,9,n,2,d"
ls = s.split(",")
ls_letters = []
ls_digits = []
for l in ls:
  if l in string.digits:
    ls_digits.append(l)
  else:
    ls_letters.append(l)
print(ls_letters)
print(ls_digits)