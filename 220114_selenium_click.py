#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import os

url_wenqian = "https://reurl.cc/9O5jpx"
target_string = "歐元問世風雨廿年 挺過金融風暴與歐債危機 TVBS文茜的世界周報-歐洲版 20220108 X 富蘭克林‧國民的基金"
app = "Preview.app"

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(url_wenqian)
driver.find_element(By.LINK_TEXT, target_string).click()
sleep(3)

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
driver.save_screenshot('sean-%s.png' % now)
cmd_save_png = f'open sean-{now}.png'
os.system(cmd_save_png)
sleep(3)
cmd_close_png = f'kill $(ps aux | grep {app} | tr -s ' ' | cut -d ' ' -f 2)'
os.system(cmd_close_png)
driver.quit()

#############################################3

"""
《V1》
from selenium import webdriver
import selenium

chrome_driver = "/usr/local/bin/chromedriver"
url_wenqian = "https://reurl.cc/9O5jpx"
target_string = "美國淡出 中東國家另覓新盟友 法中成新歡 TVBS文茜的世界"

browser = webdriver.Chrome(chrome_driver)
browser.get(url_wenqian)
browser.find_element_by_link_text(target_string).click()
"""

#####################################333

"""
下載pip的tar.gz檔，解壓縮後，丟去which python3的目錄位置，然後那個目錄下執行
$ python pip install （python 檔案名稱 指令參數1）
$ pip3 install selenium
到Chrome的「說明」，關於 Chrome，
版本 97.0.4692.71 (正式版本) (x86_64)，
然後到這個網址下載跟自己版本相同的Driver：
http://chromedriver.chromium.org/
下載好之後，會是一個壓縮檔，解壓縮之後，
點開 Finder，按「command+shift+G」，這個指令可以開啟隱藏資料夾，
然後把chromedriver這個Unix執行檔放到「/usr/local/bin」，資料夾下。
"""

"""
《截圖》
$ open -a Photos test.jpg 
import test.jpg 到 Photos
不過要先安裝Pixelmator

>>> from selenium import webdriver
>>> from datetime import datetime
>>> now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
>>> driver.save_screenshot('login-%s.png' % now)

>>> from subprocess import call
>>> call(["screencapture", "screenshot.jpg"])   # full screen
>>> call(["screencapture", "-i", "/Users/user/Documents/screenshot.jpg"])
>>> call(["screencapture", "-R 100,100,500,500", "screenshot.jpg"]) # partial screen

部分截圖
$ screencapture -R100,100,500,500 asdf.png
# pixels: (500-100)x(500-100) 
# file name: asdf.png
"""