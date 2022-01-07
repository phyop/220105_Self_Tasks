# 在2*100的表格中，隨意產生數值或是空白，輸出csv檔案

"""
思考解法：
用numpy產生2*100的ndarray
先全部填入亂數 -> 怎麼設亂數？
然後再隨機選取30%的元素，設成空白(NA) -> 怎麼設NA？
np.savetxt輸出
"""


"""
《numpy - 輸出txt》
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

---------------------------

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

------------------------------

"""
《随机选择list或array中n个元素》
https://blog.csdn.net/weixin_44633882/article/details/103748747

random.choice(列表) # 從列表中随机选取一个元素
random.sample(列表, 取數) # 结果每次运行结果不同
「4. 从numpy.ndarray中随机选取多个元素」 -> 可以參考，但自己想怎麼寫，會比看他的code有效率
"""

------------------------------

"""
《Dataframe.to_csv() 、 writer.writerows()》
https://www.delftstack.com/zh-tw/howto/python/python-write-array-to-csv/

"""