# -*- coding: utf-8 -*-
# @Author   : liu
import requests
import os
import io
import sys
import multiprocessing
import json
from datetime import datetime
from multiprocessing import Pool
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

'''
render是get方式
execute是post方式
'''

def splash_render(url):

    '''
    args参数说明：
    url: 需要渲染的页面地址
    timeout: 超时时间
    proxy：代理
    wait：等待渲染时间
    images: 是否下载，默认1（下载）
    js_source: 渲染页面前执行的js代码
    '''
    splash_url = "http://localhost:8050/render.html"

    args = {
        "url": url,
        "timeout": 5,
        "image": 0
    }

    response = requests.get(splash_url, params=args)
    return response.text


def splash_execute(url):
    '''
    参数说明：
    timeout 超时
    lua_source lua脚本
    proxy 代理

    '''
    splash_url = "http://localhost:8050/execute"

    script = """
    function main(splash)
        local url="{url}"
        splash:set_user_agent("Mozilla/5.0  Chrome/69.0.3497.100 Safari/537.36")
        splash:go(url)
        splash:wait(2)
        splash:go(url)
        return {
            html = splash:html()
        }
    end
    """
    script = script.replace("{url}", url)
    data = json.dumps({
        "timeout": 5,
        "lua_source": script
    })

    headers = {
        "User-Agent": "Mozilla/5.0 Chrome/69.0.3497.100 Safari/537.36",
        "content-type": "application/json"
    }

    response = requests.post(splash_url, headers=headers, data=data)

    return response.json().get("html")


splash_url = "http://127.0.0.1:8050/render.html"  # splash地址

headers = {
    # "User-Agent": "9999999",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "ub": "111"
}

def parse_page(response):
    """回调解析"""
    print(response)


def run(url):
    """..."""
    try:
        params = {
            "url": url,
            "http_method": "GET",
            "image": 0,
            "timeout ": 30,
            'headers': headers,
        }
        response = requests.post(splash_url,headers={'Content-Type': 'application/json'}, data=json.dumps(params)).text
    except Exception as e:
        print(e)
    else:
        return (url,response)

if __name__ == "__main__":
    pool = Pool(5)  # 5个进程池
    # obtain_list = ["http://httpbin.org/get"] * 20  # 请求地址
    obtain_list = ["https://www.baidu.com"] * 20  # 请求地址
    for i in obtain_list:
        pool.apply_async(run, (i,), callback=parse_page)
    pool.close()
    pool.join()