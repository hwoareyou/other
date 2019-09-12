import requests,random

def get_proxy():

    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9020"


    proxyUser = "HIL217ZFCDHGJ6FD"
    proxyPass = "1375697BCADCD8BB"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http" : proxyMeta,
        "https" : proxyMeta,
    }

    return proxies




if __name__ == '__main__':
    get_proxy()