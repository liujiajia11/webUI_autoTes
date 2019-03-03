from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time
import unittest
class FristDisciz(BasePage):
    #登录内容
    username_serach_loc=(By.ID,"ls_username")
    password_search_loc=(By.ID,"ls_password")
    login_button_search_loc=(By.TAG_NAME,"em")
    uesrname_button_search_loc = (By.CSS_SELECTOR, ".vwmy a")
    #默认板块
    default_plate_search_loc=(By.XPATH,"//tr[1]/td/h2/a")
    #发帖内容
    title_search_loc=(By.ID,"subject")
    fatie_message_search_loc=(By.ID,"fastpostmessage")
    fatei_button_search_loc=(By.XPATH,"//p/button/strong")
    fatie_title_text_search_loc=(By.CSS_SELECTOR,".ts span")
    #回帖内容
    huitie_search_loc=(By.ID,"post_reply")
    huitie_message_search_loc=(By.ID,"postmessage")
    huitie_button_search_loc=(By.XPATH,"//p/button/strong")
    #退出
    logout_button_search_loc=(By.LINK_TEXT,"退出")

    def login(self,username,password):
        self.sendkeys(username,*self.username_serach_loc)
        self.sendkeys(password,*self.password_search_loc)
        self.click(*self.login_button_search_loc)
        time.sleep(5)
        except_value1 = self.get_text(self.find_element(*self.uesrname_button_search_loc))
        unittest.TestCase().assertEqual(except_value1, username, username)
    def default_plate(self):
        time.sleep(5)
        self.click(*self.default_plate_search_loc)
    def fatie(self,title,content):
        time.sleep(2)
        self.sendkeys(title,*self.title_search_loc)
        self.sendkeys(content,*self.fatie_message_search_loc)
        self.click(*self.fatei_button_search_loc)
        time.sleep(2)
        except_value=self.get_text(self.find_element(*self.fatie_title_text_search_loc))
        unittest.TestCase().assertEqual(except_value,title,title)
    def huitie(self,content):

        self.click(*self.huitie_search_loc)
        self.sendkeys(content,*self.huitie_message_search_loc)
        self.click(*self.huitie_button_search_loc)
    def logout(self):
        self.click(*self.logout_button_search_loc)

