from appium import webdriver

from time import sleep

class Action():

    def __init__(self):

        # 初始化配置，设置Desired Capabilities参数

        self.desired_caps = {

              "platformName": "Android",
              "deviceName": "127.0.0.1:62001",
              "appPackage": "com.ss.android.ugc.aweme",
              "appActivity": ".main.MainActivity",
              "platformVersion": "5.1.1"

        }

        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)


        # caps = {}
        # caps["platformName"] = "Android"
        # caps["deviceName"] = "127.0.0.1:62001"
        # # Next two ele can be found by bash command:
        # # adb logcat ActivityManager:I*:s
        # caps["appPackage"] = "com.ss.android.ugc.aweme"  # DouYin package adress
        # caps["appActivity"] = ".main.MainActivity"  # DouYin lauching activity
        # caps["newCommandTimeout"] = 0
        # # Remote driver connection to appium server
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        # 设置滑动初始坐标和滑动距离(距离设置过大会报错)
        self.start_x = 300
        self.start_y = 700
        self.distance = 300

    def comments(self):
        sleep(2)
        # app开启之后点击一次屏幕，确保页面的展示
        self.driver.tap([(30, 500)], 500)

    def scroll(self):
        # 无限滑动
        while True:
            # 模拟滑动
            self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance)
            # 设置延时等待
            sleep(2)
            try:
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/cun').click()
                print('存在购物车,点击查看商品详情！')

            except:
                continue

    def main(self):
        # self.comments()
        self.scroll()




        # self.driver.swipe(510, 50, 510, 50)  # 搜索
        # self.driver.swipe(500, 575, 100, 575)  # 滑动（右→左）
        # self.driver.swipe(510, 575, 510, 575)  # 好物榜
        # self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/cj5') # 点击好物榜

if __name__ == '__main__':

    action = Action()
    action.main()

'''
com.ss.android.ugc.aweme:id/d8_ 上部
com.ss.android.ugc.aweme:id/ip  下部（名字、内容、定位、说明）
com.ss.android.ugc.aweme:id/ci6 右下部（点赞、评论、转发）
com.ss.android.ugc.aweme:id/bnq 底部（首页、关注、消息、我）

com.ss.android.ugc.aweme:id/cun 购物车
com.ss.android.ugc.aweme:id/b1b 搜索按钮

（510,50） 搜索按钮   self.driver.swipe(510,50,510,50) # 搜索
（500,575）-（100,575）  self.driver.swipe(500,575,100,575) # 滑动（右→左）
                        self.driver.swipe(510,575,510,575)  # 好物榜
'''