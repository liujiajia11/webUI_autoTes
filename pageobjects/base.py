from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os.path
import unittest
from framework.logger import Logger

logger=Logger(logger="BasePage").getlog()   #logger实例化对象

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        """浏览器后退按钮"""
        self.driver.back()
        logger.info("click back on current page")
    def forward(self):
        """浏览器前进按钮"""
        self.driver.forward()
        logger.info("click forward on current page")
    def open_url(self,url):
        """打开URL"""
        self.driver.get(url)
    def quit_browser(self):
        """点击关闭浏览器"""
        self.driver.quit()
    def close(self):
        """点击关闭当前窗口"""
        try:
            self.driver.close()
            logger.info("Closing and quit this browers.")
        except Exception as e:
            logger.error("Failed to quit the browers with %s" % e)
    def find_element(self,*loc):
        """查找元素"""
        try:
           WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
           logger.info("找到页面元素%s", loc)
           return self.driver.find_element(*loc)        #当页面在加载的时候定位元素
        except:
            logger.error("%s 页面中找不到 %s元素" %(self,loc))
    def F5(self):
         self.driver.refresh()
    def get_windows_img(self):
        """屏幕截图"""
        file_path=os.path.dirname(os.path.abspath('.'))+"/screenshots/"
        nq=time.strftime("%y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+nq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("take screenshot and save to floder")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s"% e)

    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容:%s",text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def get_text(self,content):
        """得到该元素的文本内容"""
        try:
            con = content.text
            logger.info("取得的内容:%s",content)
            return con
        except Exception as e:
            logger.error("Failed to get element with %s" % e)
            self.get_windows_img()

    def open_first_window(self):
        """激活打开的第二个窗口"""
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            logger.info("Activate first window")
        except:
            logger.error("Failed to activate first window")
    def open_second_window(self):
        """激活打开的第二个窗口"""
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.info("Activate second window")
        except:
            logger.error("Failed to activate second window")
    def switch_to_frame(self):
        try:
            self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
            logger.info("Succerfully switch to frame")
        except:
            logger.error("Failed to switch to frame")
    def switch_to_frame_out(self):
        """退出iframe，回到上层"""
        try:
            self.driver._switch_to.default_content()
            logger.info("Succerfully switch to frame")
        except:
            logger.error("Failed to switch to frame")
    def hover_element(self,*loc):
        """鼠标悬浮于元素"""
        ActionChains.move_to_element(*loc).perform()
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("Clear text in input box before typing")
        except Exception as e:
            logger.error("Failed to clear text in input box with %s" %e)
            self.get_windows_img()
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("The element was click ")
        except Exception as e:
            logger.error("Failed to clickelement with %s" %e)


