from selenium import webdriver
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
options=webdriver.ChromeOptions()
options.add_argument('user-agent= ' + ua)
driver=webdriver.Chrome(options=options)
driver.get('http://httpbin.org/user-agent')