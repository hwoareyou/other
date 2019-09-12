import os
import requests,re,random,time
from PIL import Image
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from  mysql_utils.mysql_db import MysqlDb
from tengxun_OCR import Ocr
import warnings
warnings.filterwarnings('ignore')
mysql = MysqlDb()


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

def get_headers():
    headers = {
        "Host": "www.amazon.com",
        # "Connection": "keep-alive",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":get_useragent(),
        "Referer": "www.amazon.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Cookie": cookie ,
        "Cookie": 'session-id=144-3995449-1647815; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; ubid-main=131-4704024-1481156; x-wl-uid=11pI1R8AVx1DhVjYPNqpO1wdTNilckVannUorKn0kTNwC/9W0omYFKqd7poB5OES9mnwKfD4c/Iw=; session-token=lJzTNP+ST89Hf15FrcRq4hMrf2wXixD7gNw8oLVCeTHeombHt+dTEu99kiQl++j3NKWnx2N5h5mldqo2Sdm1WcqVhPZOy2pbIuQdrLFwHhLhDt69DZAyON5JiNxW69WXOP4iPoQFxZyFznxrfYFMtTHPIr8ls2XMY31zsQ1Y/xl2H2qVOmGGuVK+ikpGIp9+MuYqpclWKUkukD53mbY7IHGFVuxrOLPb1+1ME7jl2j5p/lPMhnHPoiEGG5wjjEYO; skin=noskin; lc-main=en_US; csm-hit=tb:FJPRNNZKZNCFYCEB7QS7+s-FJPRNNZKZNCFYCEB7QS7|1563361913768&t:1563361913768&adb:adblk_no'

    }
    return  headers

def request(i,keyword,headers):
    post_data = {
        "i": "aps",
        "k": keyword,
        "ref": "nb_sb_noss",
        "url": "search-alias=aps",
    }
    url = 'https://www.amazon.com/s?i=aps&ref=nb_sb_noss&url=search-alias%3Daps&k=' + keyword

    if i >= 50:
        headers = get_headers()
        i = 0
    try:
        rest = requests.post(url, headers=headers, data=post_data, timeout=20)
    except:
        count = 1
        while count <= 5:
            try:
                rest = requests.post(url, headers=headers, data=post_data, timeout=20)
                break
            except:
                err_info = 'requests reloading for %d time' % count if count == 1 else 'requests reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 5:
            print("requests job failed!")
            result = getAmazonResultNumber(url)
            sql = 'update amazonshop_keywords set result_volume = %s WHERE keyword_name = %s '
            mysql.update(sql, [(result, keyword)])
            print('keyword:%s,result:%s' % (keyword, result))

    return rest, url, i


headers = {
        "Host": "www.amazon.com",
        # "Connection": "keep-alive",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":get_useragent(),
        "Referer": "www.amazon.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Cookie": cookie ,
        "Cookie": 'session-id=144-3995449-1647815; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; ubid-main=131-4704024-1481156; x-wl-uid=11pI1R8AVx1DhVjYPNqpO1wdTNilckVannUorKn0kTNwC/9W0omYFKqd7poB5OES9mnwKfD4c/Iw=; session-token=lJzTNP+ST89Hf15FrcRq4hMrf2wXixD7gNw8oLVCeTHeombHt+dTEu99kiQl++j3NKWnx2N5h5mldqo2Sdm1WcqVhPZOy2pbIuQdrLFwHhLhDt69DZAyON5JiNxW69WXOP4iPoQFxZyFznxrfYFMtTHPIr8ls2XMY31zsQ1Y/xl2H2qVOmGGuVK+ikpGIp9+MuYqpclWKUkukD53mbY7IHGFVuxrOLPb1+1ME7jl2j5p/lPMhnHPoiEGG5wjjEYO; skin=noskin; lc-main=en_US; csm-hit=tb:FJPRNNZKZNCFYCEB7QS7+s-FJPRNNZKZNCFYCEB7QS7|1563361913768&t:1563361913768&adb:adblk_no'

    }

# 识别验证码
def get_character_by_ocr():
    try:
        print('出现验证码，正在验证！')
        # 最多进行10次验证
        for i in range(10):
            # 验证码截图
            img_path = os.getcwd() + '/verification/verification_code.png'
            driver.get_screenshot_as_file(img_path)
            try:
                element = driver.find_element_by_xpath(
                    '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]')
            except:
                print('验证成功！')
                return True

            # 计算出元素上、下、左、右 位置
            left = element.location['x']
            top = element.location['y']
            right = element.location['x'] + element.size['width']
            bottom = element.location['y'] + element.size['height']

            im = Image.open(img_path)
            im = im.crop((left, top, right, bottom))
            im.save(img_path)

            # 识别验证码
            tengxun_ocr = Ocr()
            character = tengxun_ocr.recognition_character(img_path)
            print('识别验证码：', character)

            # 验证码输入
            driver.find_element_by_xpath('//*[@id="captchacharacters"]').send_keys(character)
            time.sleep(3)
            # 验证
            driver.find_element_by_xpath(
                '/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button').click()
        else:
            return False

    except Exception as err:
        print(err)

def getAmazonResultNumber(url):
    try:
        driver.get(url)
    except:
        count = 1
        while count <= 5:
            try:
                driver.get(url)
                break
            except:
                err_info = 'driver.get() reloading for %d time' % count if count == 1 else 'driver.get() reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 5:
            print("driver.get() job failed!")
    finally:
        title = driver.title
        if title == 'Robot Check':
            flag = get_character_by_ocr()
            if flag:
                driver.get(url)
            else:
                return 'NULL'
        time.sleep(random.random())
        try:
            result_number = driver.find_element_by_xpath('//*[@id="search"]/span/h1/div/div[1]/div/div/span[1]').text
            result_number = re.search(r'([,\d]+) result', result_number).group(1).replace(',', '')
        except:
            result_number = 0
        # result_number = re.search(r'共.*?(\d+,\d+|\d+)',result_number).group(1).replace(',','')
        # driver.delete_all_cookies()
        return result_number

# service_args = ['--ssl-protocol=any', '--cookies-file=False']
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
# )
# driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)

#创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
#设置浏览器参数
chrome_options.add_argument('--headless')  # 无界面
chrome_options.add_argument('--no-sandbox') # 让Chrome在root权限下跑
chrome_options.add_argument('--disable-dev-shm-usage')
#创建浏览器对象
driver = webdriver.Chrome(chrome_options=chrome_options)


def main(headers):
    sql = 'select keyword_name from amazonshop_keywords WHERE id >= 5212 and result_volume IS NULL '
    res = mysql.select(sql)
    if res:
        i = 0
        for data in res:
            i += 1
            keyword = data['keyword_name']
            # keyword = 'shirt'
            print('request:',keyword)
            try:
                rest , url, i = request(i,keyword,headers)
            except:
                continue
            html = rest.text
            title = re.search(r'<title[ dir="ltr"]*>(.+)</title>',html)
            if title:
                print('title')
                title = title.group(1)
                if title == 'Robot Check':
                    print('Robot Check')
                    result = getAmazonResultNumber(url)
                else:
                    result = re.search(r'"totalResultCount":([,\d]+),', html)
                    if result:
                        result = result.group(1)
                    else:
                        result = 0
            else:
                print('no-title')
                result = 0
            sql = 'update amazonshop_keywords set result_volume = %s WHERE keyword_name = %s '
            mysql.update(sql,[(result, keyword)])
            print('keyword:%s,result:%s'%(keyword, result))


if __name__ == '__main__':
    main(headers)