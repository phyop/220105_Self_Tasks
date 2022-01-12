#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# 在2*100的表格中，隨意產生數值或是空白，輸出csv檔案

import numpy as np
import random

m, n = 10, 2 # np.array(m*n)
digits = 100 # 幾位數 = len（10^N）-1
probability = 0.2

a = digits*np.random.random((m,n))
a = np.floor(a) # 取整數
# 隨機取得xx%的索引位置 = random.sample(列表， int（xx% x 列表長度)）
index_0 = [i for i in range(a.shape[0])]
index_1 = [i for i in range(a.shape[1])]
choose_num = int(probability * m * n) # 其實len(index_0)就是a.shape[0]
while True:
    randIndex_0 = np.random.choice(index_0, choose_num) 
    randIndex_1 = np.random.choice(index_1, choose_num) 
    randIndex = list(zip(randIndex_0, randIndex_1))
    for i in randIndex:
        a[i[0],i[1]] = np.nan
    if len(a[np.isnan(a)]) == choose_num: # 非Nan的个数 = len(a[~np.isnan(a)])
        break
print("probability = ", probability)
print("number of nan = ", choose_num)
print(a)

# 計算nan的數量
# count = 0
# for i in range(a.shape[0]):
#     for j in range(a.shape[1]):
#         if a[j,i][a[j,i] != a[j,i]]:  # workable， but deprecated
#             count += 1
# print('count = ',count)





"""
思考解法：
用numpy產生100*2的ndarray -> np.array([3,2],...)
先全部填入亂數 -> random.random()
然後再隨機選取30%的元素，設成空白(NA) -> np.nan
np.savetxt輸出
"""

############################################

"""
《隨機抽取》
https://blog.csdn.net/DSTJWJW/article/details/90667570

random.sample() 和 numpy.random.choice() 的优点都是可以指定抽样的个数，
一次性从列表中不重复地抽样出指定个数的元素，
其中 random.sample()默认就是不重复抽样（不放回的抽样），
而numpy.random.choice()默认是可以重复抽样，
要想不重复地抽样，需要设置replace参数为False。

当数量较少的时候，random.sample() 用时非常少，而numpy.random.choice()则很长；
当抽样数量很大的时候，numpy.random.choice()几乎不变，而random.sample() 用时变长。

"""

############################################

"""
https://www.itread01.com/content/1553930535.html
提取隨機數組中的整數部分
print (np.trunc(Z))
print (np.floor(Z))
print (Z.astype(int))
"""

############################################

"""
《np.nan》
https://reurl.cc/AKkGzY

bool(np.nan != np.nan)
#返回 True
#在numpy中每個nan皆為獨特的存在

bool（a!=a） (同 np.isnan(a))
僅有nan與nan不相等
因此nan位置會為True 其餘返回False

a=np.array([1,2,3,4,5,6],dtype=float).reshape(2,3) # nan為float 因此需定義類型
a[1,1]=np.nan # 創建一含nan 數組
result=np.count_nonzero(a!=a) # 計算數組中不為0的數量
# 同result=np.count_nonzero(np.isnan(a))
# 計算nan數量

《將某數組中的nan替換為該column 平均值方法》
a[a != a] =10 # 即可將nan替換為10
valid = a[a == a] # 回傳所有不為nan的值

for i in range(a.shape[1]):
    if a[:,i][a[:,i] != a[:,i]]: # 如果是nan，則用平均值去取代
    # 就是a[a!=a]的操作，只不過把a改成了a[:,i]
        group_mean= a[:,i][a[:,i] == a[:,i]].mean() # a[a == a] 將非nan值取平均
        a[:,i][a[:,i] != a[:,i]] = group_mean
"""

############################################

"""
《numpy - 輸出txt》
import numpy as np
a = np.array([[1,4,2],[7,9,4],[0,6,2]])
np.savetxt('test.csv', a, delimiter=',') # 1.000000000000000000e+00
np.savetxt('test.csv', a, delimiter=',',fmt='%f') 1.00000
fmt='%.1f' # 1.0
fmt='%d' # 1
fmt='%1.4e' # use exponential notation
header - 將在文件開頭寫入的字符串。
footer - 將在文件末尾寫入的字符串。
comments - 將前綴到 header 和 footer 字符串的字符串，將它們標記爲註釋。默認值:’ # '，如numpy.loadtxt所期望的那樣。
"""

############################################

"""
《savetxt - 三維破解法》
https://stackoverflow.com/questions/3685265/how-to-write-a-multidimensional-array-to-a-text-file

import numpy as np
x = np.arange(20).reshape((4,5))
np.savetxt('test.txt', x)


np.savetxt對於 3D 數組，同樣的事情會失敗
import numpy as np
x = np.arange(200).reshape((4,5,10))
np.savetxt('test.txt', x)
一種解決方法是將 3D（或更大）陣列分解為 2D 切片。例如

x = np.arange(200).reshape((4,5,10))
with open('test.txt', 'w') as outfile:
    for slice_2d in x:
        np.savetxt(outfile, slice_2d)
但是，我們的目標是清晰易讀，同時仍然可以輕鬆地用. 因此，我們可以更詳細一些，並使用註釋掉的行來區分切片。默認情況下，將忽略以#（或kwarg指定的任何字符）開頭的任何行。

import numpy as np
import random

# Generate some test data
data = np.arange(200).reshape((4,5,10))

# Write the array to disk
with open('test.txt', 'w') as outfile:
    # I'm writing a header here just for the sake of readability
    # Any line starting with "#" will be ignored by numpy.loadtxt
    outfile.write('# Array shape: {0}n'.format(data.shape))
    
    # Iterating through a ndimensional array produces slices along
    # the last axis. This is equivalent to data[i,:,:] in this case
    for data_slice in data:

        # The formatting string indicates that I'm writing out
        # the values in left-justified columns 7 characters in width
        # with 2 decimal places.  
        np.savetxt(outfile, data_slice, fmt='%-7.2f')

        # Writing out a break to indicate different slices...
        outfile.write('# New slicen')
這產生：

# Array shape: (4, 5, 10)
0.00    1.00    2.00    3.00    4.00    5.00    6.00    7.00    8.00    9.00   
10.00   11.00   12.00   13.00   14.00   15.00   16.00   17.00   18.00   19.00  
20.00   21.00   22.00   23.00   24.00   25.00   26.00   27.00   28.00   29.00  
30.00   31.00   32.00   33.00   34.00   35.00   36.00   37.00   38.00   39.00  
40.00   41.00   42.00   43.00   44.00   45.00   46.00   47.00   48.00   49.00  
# New slice
50.00   51.00   52.00   53.00   54.00   55.00   56.00   57.00   58.00   59.00  
60.00   61.00   62.00   63.00   64.00   65.00   66.00   67.00   68.00   69.00  
70.00   71.00   72.00   73.00   74.00   75.00   76.00   77.00   78.00   79.00  
80.00   81.00   82.00   83.00   84.00   85.00   86.00   87.00   88.00   89.00  
90.00   91.00   92.00   93.00   94.00   95.00   96.00   97.00   98.00   99.00  
# New slice
100.00  101.00  102.00  103.00  104.00  105.00  106.00  107.00  108.00  109.00 
110.00  111.00  112.00  113.00  114.00  115.00  116.00  117.00  118.00  119.00 
120.00  121.00  122.00  123.00  124.00  125.00  126.00  127.00  128.00  129.00 
130.00  131.00  132.00  133.00  134.00  135.00  136.00  137.00  138.00  139.00 
140.00  141.00  142.00  143.00  144.00  145.00  146.00  147.00  148.00  149.00 
# New slice
150.00  151.00  152.00  153.00  154.00  155.00  156.00  157.00  158.00  159.00 
160.00  161.00  162.00  163.00  164.00  165.00  166.00  167.00  168.00  169.00 
170.00  171.00  172.00  173.00  174.00  175.00  176.00  177.00  178.00  179.00 
180.00  181.00  182.00  183.00  184.00  185.00  186.00  187.00  188.00  189.00 
190.00  191.00  192.00  193.00  194.00  195.00  196.00  197.00  198.00  199.00 
# New slice
只要我們知道原始數組的形狀，讀回它就很容易。我們只能做。舉個例子（你可以在一行中做到這一點，我只是為了澄清事情而冗長）：numpy.loadtxt('test.txt').reshape((4,5,10))

# Read the array from disk
new_data = np.loadtxt('test.txt')

# Note that this returned a 2D array!
print new_data.shape

# However, going back to 3D is easy if we know the 
# original shape of the array
new_data = new_data.reshape((4,5,10))
    
# Just to check that they're the same...
assert np.all(new_data == data)
"""

############################################

"""
《随机选择list或array中n个元素》
https://blog.csdn.net/weixin_44633882/article/details/103748747

random.choice(列表) # 從列表中随机选取一个元素
random.sample(列表, 取數) # 结果每次运行结果不同

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
label = [0, 1, 2, 3, 4, 5, 6, 7]
sample_num = int(0.5 * len(data)) # 假设取50%的数据
# 隨機取得xx%的索引位置 = random.sample(列表， int（xx% x 列表長度)）
sample_list = [i for i in range(len(data))] # [0, 1, 2, 3, 4, 5, 6, 7]
sample_list = random.sample(sample_list, sample_num) #随机选取出了 [3, 4, 2, 0]
sample_data = [data[i] for i in sample_list] # ['d', 'e', 'c', 'a']
sample_label = [label[i] for i in label] # [3, 4, 2, 0]

「4. 从numpy.ndarray中随机选取多个元素」 -> 可以參考，但自己想怎麼寫，會比看他的code有效率
"""

############################################

"""
《Dataframe.to_csv() 、 writer.writerows()》
https://www.delftstack.com/zh-tw/howto/python/python-write-array-to-csv/

# Dataframe.to_csv(path, sep,...)
df = pandas.DataFrame(myarray)
df.to_csv('myfile.csv')

# csv.writer.writerows(rows) 
import csv
a = numpy.array([[1,4,2],[7,9,4],[0,6,2]])
with open('myfile.csv', 'w', newline='') as file: # file是檔案物件
    mywriter = csv.writer(file, delimiter=',') # mywriter是csv物件
    mywriter.writerows(a)

# csv.reader(file)
with open('myfile.csv', 'r', newline='') as file:
  myreader = csv.reader(file, delimiter=',') # csv要去獲取檔案物件，才能變成cvs物件
  for rows in myreader:
    print(rows)
"""