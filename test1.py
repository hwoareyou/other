# -*- coding:utf-8 -*-

import requests
import warnings
import random
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

warnings.filterwarnings('ignore')


class ClawerLazada():

    def __init__(self):

        chrome_options = Options()
        chrome_options.binary_location = r'C:\Users\panda\Desktop\ChromePortable\App\Google Chrome\chrome.exe'
        # 创建浏览器对象
        self.driver = webdriver.Chrome(executable_path=r"D:\ProgramData\Anaconda3\Scripts\chromedriver.exe",chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()

    def __request_parent_keyword__(self):
        headers = {
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            "Accept-Encoding": 'gzip, deflate, br',
            "Accept-Language": 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            "Connection": 'keep-alive',
            "Host": 'www.lazada.co.th',
            "Upgrade-Insecure-Requests": '1',
            "User-Agent": get_useragent()
        }
        kw = {
            'spm': 'a2o4m.searchlist.header.dhome.73c9748fYdCvPH'
        }
        response = requests.get("https://www.lazada.co.th/?", params=kw, headers=headers).content.decode()

        tree = etree.HTML(response)

        # 定义一个热词总列表
        hot_keywords_list = []

        # 第一层热词
        first_xpath = "//ul[@ class ='lzd-site-menu-root'] / li[@ class='lzd-site-menu-root-item'] / a / span / text()"
        first_hot_keywords = tree.xpath(first_xpath)

        # 循环第一层热词，添加到热词总列表
        for first_hot_keyword in first_hot_keywords:
            hot_keywords_list.append(first_hot_keyword)

        # 第二层热词
        second_xpath = "//ul[@ class ='lzd-site-menu-root'] / ul / li / a / span / text()"
        second_hot_keywords = tree.xpath(second_xpath)

        # 循环第二层热词，添加到热词总列表
        for second_hot_keyword in second_hot_keywords:
            hot_keywords_list.append(second_hot_keyword)

        # 第三层热词
        third_xpath = "//ul[@ class ='lzd-site-menu-root'] / ul / li / ul / li / a / span / text()"
        third_hot_keywords = tree.xpath(third_xpath)

        # 循环第三层热词，添加到热词总列表
        for third_hot_keyword in third_hot_keywords:
            hot_keywords_list.append(third_hot_keyword)

        # 去重热词总列表
        hot_keywords_list = list(set(hot_keywords_list))

        return hot_keywords_list

    def __selenium_children_keyword__(self, keyword):
        # time.sleep(random.randint(1, 3))
        self.driver.get("https://www.lazada.co.th/?spm=a2o4m.searchlist.header.dhome.73c9748fYdCvPH#")
        node = self.driver.find_element_by_xpath("//input[@id='q']")
        node.send_keys("อุปกร")
        print(self.driver.find_element_by_id("q").text)
        pass



def get_useragent():
    useragent_list = [
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    return random.choice(useragent_list)


def main():
    pass


def run():
    clawer_lazada = ClawerLazada()
    # hot_keywords_list = clawer_lazada.__request_parent_keyword__()
    clawer_lazada.__selenium_children_keyword__('อุปกรณ์')


if __name__ == '__main__':
    # all_keywords = [['diy logo hoodie print'], ['diy logo tee shirt print'], ['diy logo mugs print'], ['diy logo hoodies'], ['diy logo tee shirt'], ['diy star hoodies'], ['diy star tee shirt '], ['logo hoodies printed'], ['logo tee shirt printed']]
    # for data in all_keywords:
    #     keyword = data[0]
    #     run(keyword)
    # print('数据采集完成！')
    run()
