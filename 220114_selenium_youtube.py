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
from selenium.webdriver.common.action_chains import ActionChains
# pip install webdriver-manager

def chrome_get(url):
    # 用Chrome當driver，打開url
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    driver.maximize_window()
    return driver

def load_json(file_json):
    # 讀取json檔的cookie
    with open(file_json) as f:
        cookies = json.load(f)
    sleep(1)
    return cookies

def add_cookies(driver, cookies):
    # 載入cookie到driver
    for cookie in cookies:
        driver.add_cookie(cookie)
    sleep(1)
    driver.refresh() # 重新整理頁面

def scroll_down(driver,times):
    for i in range(times):
        driver.execute_script(f"window.scrollBy(0,{100*times})")
        sleep(1)

def click_hidden_menu(driver, title_xpath, hidden_menu_xpath):
    scroll_down(driver,1)
    title = driver.find_element(By.XPATH, title_xpath)
    hidden_menu = driver.find_element(By.XPATH, hidden_menu_xpath)
    ActionChains(driver).move_to_element(title).click(hidden_menu).perform()

if __name__ == '__main__':
    url_wenqian = "https://reurl.cc/9O5jpx"
    cookie_json = "210118_youtube_nameValue.json"
    title_xpath = "//ytd-grid-video-renderer[1]//h3/a"
    hidden_menu_xpath = "//ytd-grid-video-renderer[1]/div[1]/div[1]/div[2]/ytd-menu-renderer/yt-icon-button/button"
    
    driver = chrome_get(url_wenqian)
    cookies = load_json(cookie_json)
    add_cookies(driver, cookies)
    click_hidden_menu(driver, title_xpath, hidden_menu_xpath)

#################################################

""" 
# 搜尋標題&點擊
target_string = "歐元問世風雨廿年 挺過金融風暴與歐債危機 TVBS文茜的世界周報-歐洲版 20220108 X 富蘭克林‧國民的基金"
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
app = "Preview.app"
cmd_close_png = f'kill $(ps aux | grep {app} | tr -s ' ' | cut -d ' ' -f 2)'
os.system(cmd_close_png)
driver.quit()
# 點擊第i個影片
title = f"//ytd-grid-renderer/div[1]/ytd-grid-video-renderer[{i}]//h3/a"
driver.find_element(By.XPATH, title).click()
"""