import os
import requests,re,random,time
from PIL import Image
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from  mysql_utils.mysql_db import MysqlDb
from tengxun_OCR import Ocr
from hyper.contrib import HTTP20Adapter
import warnings
warnings.filterwarnings('ignore')



def main():
    headers={
        ":authority":"e-com.idvert.com",
        ":method":"POST",
        ":path":"/api_web/ad/list",
        ":scheme":"https",

        # "authority":"e-com.idvert.com",
        # "method":"POST",
        # "path":"/api_web/ad/list",
        # "scheme":"https",

        "accept":"application/json,text/plain,*/*",
        # "accept-encoding":"gzip,deflate,br",
        "accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "authorization":"a2d22fccbc18215e0bbd63f99a0c1951.0088345c514d8d59984d44720c81ff68",
        # "content-length":"28",
        "content-type":"application/json;charset=UTF-8",
        # "cookie":"_ga=GA1.2.1639939334.1551081500;intercom-id-ndcu3xsv=07da4b0d-ed8c-4731-9516-2593059b9e33;__cfduid=d6d1a0e2d19fdefe2f54f6d28a1e059c91553476813;platType=1;_ga=GA1.3.1639939334.1551081500;_gid=GA1.2.1247034567.1565234410;Validate_Code=8BZU4Edg5Q8A1UJ9ZltYBpNYxQdhloB0;kjbAuthKey=a2d22fccbc18215e0bbd63f99a0c1951.0088345c514d8d59984d44720c81ff68",
        "cookie":"_ga=GA1.2.1639939334.1551081500; intercom-id-ndcu3xsv=07da4b0d-ed8c-4731-9516-2593059b9e33; __cfduid=d6d1a0e2d19fdefe2f54f6d28a1e059c91553476813; platType=1; _ga=GA1.3.1639939334.1551081500; _gid=GA1.2.1247034567.1565234410; Validate_Code=8BZU4Edg5Q8A1UJ9ZltYBpNYxQdhloB0; kjbAuthKey=a2d22fccbc18215e0bbd63f99a0c1951.0088345c514d8d59984d44720c81ff68; _gat_UA-129333948-3=1",
        "dnt":"1",
        "origin":"https://e-com.idvert.com",
        "plattype":"1",
        "referer":"https://e-com.idvert.com/advertisings?language=41",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        # "user-agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",

    }
    datas={
        # "language":"41",
        # "pageNo":"3",

        "language":"41",
        "sortField":"default",
        "sortType":"desc",
    }


    url = 'https://e-com.idvert.com/api_web/ad/list'

    session = requests.session()
    session.mount(url, HTTP20Adapter())
    res = session.post(url, headers=headers, data=datas)
    # res = requests.post(url, headers=headers, data=datas)
    print(res.text)


if __name__== '__main__':
    main()
