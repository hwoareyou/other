from selenium import webdriver
from PIL import Image
from tengxun_OCR import  Ocr
import time

class Recognition():

    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1250, 840)
        js = "window.scrollTo(500,1000)"
        self.driver.execute_script(js)
        self.driver.get(url)
        pass

    def save_img(self):
        try:

            img_path = 'E:/亚马逊项目/验证码/yanzhengma.png'
            self.driver.get_screenshot_as_file(img_path)
            element = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]')

            # 计算出元素上、下、左、右 位置
            left = element.location['x']
            top = element.location['y']
            right = element.location['x'] + element.size['width']
            bottom = element.location['y'] + element.size['height']

            im = Image.open(img_path)
            im = im.crop((left, top, right, bottom))
            im.save(img_path)
            return img_path
        except Exception as err:
            # print(err)
            return False


    def recognition(self, img_path):
        # 识别验证码
        tengxun_ocr = Ocr()
        character = tengxun_ocr.recognition_character(img_path)

        # 验证码输入
        self.driver.find_element_by_xpath('//*[@id="captchacharacters"]').send_keys(character)
        time.sleep(3)
        # 验证
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button').click()

    def main(self):
        img_path = self.save_img()
        if img_path:
            self.recognition(img_path)
            return ''
        else:
            return '验证通过！'

if __name__ == '__main__':
    url = "https://www.amazon.com/errors/validateCaptcha?amzn=%2FrM3ZzxglOdKUjnFspBgJw%3D%3D&amzn-r=%2FCasual-Sleeve-T-Shirt-Fitness-Tshirts%2Fdp%2FB07KR957RK%2Fref%3Dsr_1_6%3Fqid%3D1562060449%26refinements%3Dp_4%253ACoCosly%26s%3Dapparel%26sr%3D1-6&field-keywords=%E5%A3%AB%E5%A4%A7%E5%A4%AB%E6%95%A2%E6%AD%BB%E9%98%9F"
    obj = Recognition(url)
    for i in range(10):
        flag = obj.main()
        if flag:
            print(flag)
            break
    else:
        print('验证失败！')
