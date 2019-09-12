import requests

# 蘑菇代理的隧道订单
appKey = "bmxMWEJCcWFuY0hQT0FQNjo2UDdOY0JsNTJCRnNYUXpJ"

# 蘑菇隧道代理服务器地址
ip_port = 'secondtransfer.moguproxy.com:9001'

# 准备去爬的 URL 链接
url = 'https://ip.cn'

proxy = {"http": "http://" + ip_port,"https": "https://" + ip_port}
headers = {
    "Proxy-Authorization": 'Basic '+ appKey,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}
r = requests.get("https://ip.cn", headers=headers, proxies=proxy,verify=False,allow_redirects=False)
print(r.status_code)
print(r.text)
if r.status_code == 302 or r.status_code == 301 :
    loc = r.headers['Location']
    print(loc)
    url_f = loc
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)