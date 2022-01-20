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
from selenium.common.exceptions import NoSuchElementException
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
        driver.execute_script(f"window.scrollBy(0,{50*times})")
        sleep(1)

def add2list(driver, video_ls, hidden_menu_ls, save2, play_list, video_number_in_channel):
    scroll_down(driver,2)
    i = 0
    count_except = 0
    while i < len(video_ls):
        try:
            video = driver.find_element(By.XPATH, video_ls[i])
            hidden_menu = driver.find_element(By.XPATH, hidden_menu_ls[i])
            ActionChains(driver).move_to_element(video).click(hidden_menu).perform()
            sleep(1)
            driver.find_element(By.XPATH, save2).click()
            sleep(1)
            driver.find_element(By.XPATH, play_list).click()
            sleep(1)
            ActionChains(driver).move_by_offset(30,30).click().perform()
            sleep(1)
            i += 1
        except NoSuchElementException:
            scroll_down(driver,1)
            count_except += 1
            if count_except >= 5: # 如果scroll幾次還是找不到這個序號的影片
                i += 1 # 那就跳到下一支影片
                count_except == 0
            
def videos_xpath(video_ls, video, video_number_in_channel):
    prefix = video.split("[",1)[0]
    suffix = video.split("]",1)[1]
    for i in range(8, video_number_in_channel+1):
        video = prefix + f'[{i}]' + suffix
        video_ls.append(video)
    return video_ls

if __name__ == '__main__':
    url_wenqian = "https://reurl.cc/9O5jpx"
    cookie_json = "210118_youtube_nameValue.json"
    video_ls = []
    hidden_menu_ls= []
    video = "//ytd-grid-video-renderer[1]//h3/a[contains(@aria-label,'TVBS文茜的')]"
    hidden_menu = "//ytd-grid-video-renderer[1]/div[1]/div[1]/div[2]/ytd-menu-renderer/yt-icon-button/button"
    save2 = "//ytd-menu-service-item-renderer[3]/tp-yt-paper-item/yt-formatted-string"
    play_list = "//ytd-playlist-add-to-option-renderer[2]"
    video_number_in_channel = 12

    # 加入cookie
    driver = chrome_get(url_wenqian)
    cookies = load_json(cookie_json)
    add_cookies(driver, cookies)

    # 儲存影片至播放清單
    video_ls = videos_xpath(video_ls, video, video_number_in_channel)
    hidden_menu_ls = videos_xpath(hidden_menu_ls, hidden_menu, video_number_in_channel)
    add2list(driver, video_ls, hidden_menu_ls, save2, play_list, video_number_in_channel)

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
video = f"//ytd-grid-renderer/div[1]/ytd-grid-video-renderer[{i}]//h3/a"
driver.find_element(By.XPATH, video).click()
"""