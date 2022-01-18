#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import os
import json
# pip install webdriver-manager

url_wenqian = "https://reurl.cc/9O5jpx"

# 讀取cookie的json檔
with open('210118_youtube.json') as f:
    cookies = json.load(f)
sleep(3)

# 用Chrome當driver，打開url
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(url_wenqian)
sleep(3)

# 載入cookie到driver
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get(url_wenqian)
driver.refresh() # 重新整理頁面
sleep(3)

# if __name__ == '__main__':
#     pass

#################################################

""" 
# 定義變數
app = "Preview.app"
target_string = "歐元問世風雨廿年 挺過金融風暴與歐債危機 TVBS文茜的世界周報-歐洲版 20220108 X 富蘭克林‧國民的基金"

# 搜尋標題&點擊
driver.find_element(By.LINK_TEXT, target_string).click()
sleep(3)
# 截圖
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
driver.save_screenshot('sean-%s.png' % now)
# 打開圖
cmd_save_png = f'open sean-{now}.png'
os.system(cmd_save_png)
sleep(3)
# kill圖
cmd_close_png = f'kill $(ps aux | grep {app} | tr -s ' ' | cut -d ' ' -f 2)'
os.system(cmd_close_png)
driver.quit()
"""