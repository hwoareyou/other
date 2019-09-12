import requests
import re


keyword = "diy logo tee shirt printed"

post_data = {
    "i":"aps",
    "k":keyword,
    "ref":"nb_sb_noss",
    "url":"search-alias=aps",
}

headers = {
    "Host": "www.amazon.com",
    #"Connection": "keep-alive",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" ,
    "Referer": "www.amazon.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cookie": cookie ,
    "Cookie":'session-id=144-3995449-1647815; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; ubid-main=131-4704024-1481156; x-wl-uid=11pI1R8AVx1DhVjYPNqpO1wdTNilckVannUorKn0kTNwC/9W0omYFKqd7poB5OES9mnwKfD4c/Iw=; session-token=lJzTNP+ST89Hf15FrcRq4hMrf2wXixD7gNw8oLVCeTHeombHt+dTEu99kiQl++j3NKWnx2N5h5mldqo2Sdm1WcqVhPZOy2pbIuQdrLFwHhLhDt69DZAyON5JiNxW69WXOP4iPoQFxZyFznxrfYFMtTHPIr8ls2XMY31zsQ1Y/xl2H2qVOmGGuVK+ikpGIp9+MuYqpclWKUkukD53mbY7IHGFVuxrOLPb1+1ME7jl2j5p/lPMhnHPoiEGG5wjjEYO; skin=noskin; lc-main=en_US; csm-hit=tb:FJPRNNZKZNCFYCEB7QS7+s-FJPRNNZKZNCFYCEB7QS7|1563361913768&t:1563361913768&adb:adblk_no'
}

url = 'https://www.amazon.com/s?i=aps&ref=nb_sb_noss&url=search-alias%3Daps&k='+keyword
res = requests.post(url,headers=headers,data=post_data)
html = res.text
result = re.search(r'"totalResultCount":([,\d]+),',html).group(1)
print(result)