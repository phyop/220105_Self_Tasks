"""
給一個int a[20]已排序的陣列，請寫一個function(a, size, b)，
能依照參數b(b = 0~4)別印出該區間的數字，且不包含a陣列內的元素，例如：
    b = 0, 印出0~99
    b = 1, 印出100~199
"""

import numpy as np
import random

def num_exclude(a, number, b):
    b_dict = {}
    for i  in range(-1,b+1):
        b_dict[i] = 100*(i+1)
        # {-1:0, 0:100, 1:200, 2:300, 3:400, 4:500}
    count = -1
    for i in range(b_dict[b-1], b_dict[b]):
        print(f"{i:3d}" ,end=' ') if i not in a else print('  ?', end=' ')
        count += 1
        print() if count%10 == 0 else None

if __name__ == "__main__":
    a = list(np.random.randint(0,500,size=(20)))
    b = 3
    print(sorted(a))
    num_exclude(a, 500, b)