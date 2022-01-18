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

# 自定變數
url_wenqian = "https://reurl.cc/9O5jpx"
cookie_json = "210118_youtube_nameValue.json"

def chrome_get(url):
    # 用Chrome當driver，打開url
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    driver.maximize_window()
    sleep(3)

def load_json(json_file):
    # 讀取json檔的cookie
    with open(json_file) as f:
        cookies = json.load(f)
    sleep(3)
    return cookies

def add_cookies(cookies):
    # 載入cookie到driver
    for cookie in cookies:
        driver.add_cookie(cookie)
    sleep(3)
    driver.refresh() # 重新整理頁面

if __name__ == '__main__':
    chrome_get(url_wenqian)
    cookies = load_json(cookie_json)
    add_cookies(cookies)

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