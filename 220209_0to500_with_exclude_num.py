"""
給一個int a[20]已排序的陣列，請寫一個function(a, size)能印出0~500的數字，
且不包含a陣列內的元素，請用最少的時間和空間複雜度完成。
"""
import numpy as np
import random

def num_exclude(a, number):
    count = -1
    for i in range(number+1):
        print(f"{i:3d}" ,end=' ') if i not in a else print('  ?', end=' ')
        count += 1
        print() if count%10 == 0 else None

if __name__ == "__main__":
    a = list(np.random.randint(0,500,size=(20)))
    print(sorted(a))
    num_exclude(a, 500)