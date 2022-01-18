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
