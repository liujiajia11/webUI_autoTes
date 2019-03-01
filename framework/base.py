import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from framework.logger import Logger

logger=Logger(logger="BasePage").getlog()

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #查找页面元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(loc))
            logger.info("找到页面元素--%s",loc)
            return  self.driver.find_element(*loc)
        except:
            logger.error("%s页面中没有找到%s元素"%(self,loc))
            self.get_windows_img()

    # 查找多个页面元素
    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(loc))
            logger.info("找到页面元素--%s",loc)
            return self.driver.find_elements(*loc)
        except:
            logger.error("%s页面中没有找到%s元素" % (self,loc))
            self.get_windows_img()

    # 输入
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容：%s",text)
        except Exception as e:
            logger.error("failed输入内容：%s"%e)
            self.get_windows_img()
    # 点击按钮
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("点击按钮:%s",loc)
        except:
            logger.error("点击按钮失败:%s",loc)
            self.get_windows_img()

    # 浏览器后退
    def back(self):
        self.driver.back()
        logger.info("浏览器后退")
    # 浏览器前进
    def forward(self):
        self.driver.forward()
        logger.info("浏览器前进")
    # 打开页面
    def open_url(self,url):
        self.driver.get(url)

    # 隐式等待
    def wait(self):
        self.driver.implicitly_wait(3)


    #页面中的frame
    def frame(self):
        self.driver.switch_to.frame(0)
        logger.info("发现frame")

    def quit(self):
        self.driver.quit()

    #点击关闭当前页面
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser")
        except Exception as e:
            logger.error("Failed close: %s"%e)
            self.get_windows_img()

    #激活当前窗口
    def current_window_handle(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info("激活当前窗口成功")
        except:
            logger.error("激活当前窗口失败")
            self.get_windows_img()

    #切换到第n个窗口
    def window_handle(self,num):
        try:
            self.driver.switch_to.window(self.driver.window_handles[num])
            logger.info("激活第%d个窗口成功"%num)
        except:
            logger.error("激活第%d个窗口失败"%num)
            self.get_windows_img()

    #悬停
    def move_to_element(self,*loc):
        ele=self.find_element(*loc)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            logger.info("悬停成功")
        except:
            logger.error("悬停失败")
            self.get_windows_img()

    #获取元素的text
    def text(self,element):
        el=element.text
        try:
            logger.info("获取%s元素text成功。",element)
            return el
        except:
            logger.error("获取%s元素text失败。",element)
            self.get_windows_img()

    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshorts/"
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("获得截图并保存到：/screenshorts中")
        except Exception as e:
            self.get_windows_img()
            logger.error("保存截图失败，%s"%e)





