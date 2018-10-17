#! /usr/bin/python3
# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import urllib.parse
from urllib.request import urlretrieve

import re
import html
import time
# 爬去百度图片,并保存到本地
# 需要修改的参数:1. 需要查询的图片,2. 需要保存的文件路径
class BaiduImg():

    def __init__(self, urls):
        self.baidu_url = urls['baidu']
        self.kw = urls['kw']

    def execute(self):
        browser = webdriver.Chrome()
        try:
            browser.get(self.baidu_url)
            # browser.maximize_window()
            browser.set_window_size(1840, 2224)

            # 输入查询
            text_input = browser.find_element_by_id("kw")
            text_input.send_keys(self.kw)
            text_input.send_keys(Keys.ENTER)

            page = 1
            while True:
                # 显示延迟
                wait = WebDriverWait(browser, 10)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#imgContainer")))
                # browser.find_elements_by_css_selector("")
                pattern2 = re.compile('<img class="main_img img-hover".*?src=\"(.*?)\"')
                html_content = html.unescape(browser.page_source)
                img_urls = re.findall(pattern2, html_content)
                for index, value in enumerate(img_urls):
                    timestamp = int(time.time()) + index
                    urlretrieve(value, "/home/hexin/Pictures/stamp2/"+str(timestamp)+".jpg")

            print('演示结束')
        except TimeoutException as e:
            print('request timeout, please try again later.', e.msg)
        finally:
            browser.close()


urls = {
    'kw': '动物',
    'baidu': 'http://image.baidu.com/'
}
spider = BaiduImg(urls)
spider.execute()



