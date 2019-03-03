from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time
import unittest
class ThirdDisciz(BasePage):
    # unittest.TestCase()
    #登陆
    username_text_search_loc=(By.ID,"ls_username")
    password_text_search_loc=(By.ID,"ls_password")
    login_button_search_loc=(By.TAG_NAME,"em")
    #搜索
    uesrname_button_search_loc = (By.CSS_SELECTOR, ".vwmy a")
    post_search_text_search_loc = (By.XPATH, "//input[@name='srchtxt']")
    search_button_search_loc=(By.CSS_SELECTOR,".scbar_btn_td .pn")
    post_title_search_loc=(By.XPATH,"//a/strong/font")
    #退出
    logout_button_search_loc=(By.LINK_TEXT,"退出")

    def login(self,username,password):
        self.sendkeys(username,*self.username_text_search_loc)
        self.sendkeys(password,*self.password_text_search_loc)
        self.click(*self.login_button_search_loc)
        time.sleep(5)
        except_value1 = self.get_text(self.find_element(*self.uesrname_button_search_loc))
        unittest.TestCase().assertEqual(except_value1, username, username)
    def search_post(self,postTitle):
        """搜索帖子"""
        self.sendkeys(postTitle, *self.post_search_text_search_loc)
        self.click(*self.search_button_search_loc)
        self.open_second_window()
        time.sleep(5)
        except_value=self.get_text(self.find_element(*self.post_title_search_loc))
        unittest.TestCase().assertEqual(postTitle,except_value,except_value)
        self.close()
    def logout(self):
        self.open_first_window()
        time.sleep(5)
        self.click(*self.logout_button_search_loc)
