# -*- coding: utf-8 -*-
# @Author   : liu
import json
import requests


'''
说明：
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
