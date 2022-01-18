#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# 在2*100的表格中，隨意產生數值或是空白，輸出csv檔案
"""
思考解法：
用numpy產生100*2的ndarray -> np.array([3,2],...)
先全部填入亂數 -> random.random()
然後再隨機選取30%的元素，設成空白(NA) -> np.nan
np.savetxt輸出
"""

import numpy as np
import random

m, n = 10, 2 # np.array(m*n)
digits = 100 # 幾位數 = len（10^N）-1
probability = 0.2
csvName = 'ramdon.csv'

a = digits*np.random.random((m,n))
a = np.floor(a) # 取整數
# 隨機取得xx%的索引位置 = random.sample(列表， int（xx% x 列表長度)）
index_0 = [i for i in range(a.shape[0])]
index_1 = [i for i in range(a.shape[1])]
choose_num = int(probability * m * n) # 其實len(index_0)就是a.shape[0]
# while True:
randIndex_0 = np.random.choice(index_0, choose_num) 
randIndex_1 = np.random.choice(index_1, choose_num) 
randIndex = list(zip(randIndex_0, randIndex_1))
# 因為zip結果是回傳迭代器，而for可以直接從迭代器取出，所以上面這樣寫也可以
# for i in zip(randIndex_0, randIndex_1):
for i in randIndex:
    a[i[0],i[1]] = np.nan
    # if len(a[np.isnan(a)]) == choose_num: # 非Nan的个数 = len(a[~np.isnan(a)])
    #     break
print("probability = ", probability)
print("number of nan = ", choose_num)
print(a)

np.savetxt(csvName, a, delimiter=',',fmt='%.1f')


# 計算nan的數量
# count = 0
# for i in range(a.shape[0]):
#     for j in range(a.shape[1]):
#         if a[j,i][a[j,i] != a[j,i]]:  # workable， but deprecated
#             count += 1
# print('count = ',count)


############################################
