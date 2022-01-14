#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.google.com')
driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')

#############################################3
《V1》
"""
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