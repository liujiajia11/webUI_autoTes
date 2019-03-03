from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest
class SecondDisciz(BasePage):
    # 管理员登录内容
    username_serach_loc = (By.ID, "ls_username")
    password_search_loc = (By.ID, "ls_password")
    login_button_search_loc = (By.TAG_NAME, "em")
    uesrname_button_search_loc = (By.CSS_SELECTOR, ".vwmy a")
    # 默认板块，删除帖子
    # default_plate_search_loc = (By.LINK_TEXT,"默认板块")
    default_plate_search_loc = (By.XPATH, "//tr[1]/td/h2/a")
    dagou_search_loc=(By.NAME,"moderate[]")
    delete_button_search_loc=(By.LINK_TEXT,"删除")
    sure_to_delete_button_search_loc=(By.ID,"modsubmit")
    #管理中心
    administration_center_search_loc=(By.LINK_TEXT,"管理中心")
    administration_center_password_search_loc=(By.CSS_SELECTOR,"#loginform p:nth-child(6) input")
    submit_search_loc=(By.NAME,"submit")
    #创建新的板块,退出
    disciz_button_search_loc = (By.ID, "header_forum")
    add_new_plate_search_loc=(By.CSS_SELECTOR,".lastboard .addtr")
    new_plate_name_search_loc=(By.NAME,"newforum[1][]")
    new_plate_submit_search_loc=(By.ID,"submit_editsubmit")
    new_plate_edit_search_loc=(By.LINK_TEXT,"退出")
    logout_button_search_loc = (By.LINK_TEXT, "退出")
    # 新板块
    new_plate_search_loc = (By.XPATH,"//tr[2]/td/h2/a")
    # 发帖内容
    title_search_loc = (By.ID, "subject")
    fatie_message_search_loc = (By.ID, "fastpostmessage")
    fatei_button_search_loc = (By.XPATH, "//p/button/strong")
    fatie_title_text_search_loc = (By.CSS_SELECTOR, ".ts span")
    # 回帖内容
    huitie_search_loc = (By.ID, "post_reply")
    huitie_message_search_loc = (By.ID, "postmessage")
    huitie_button_search_loc = (By.XPATH, "//p/button/strong")

    def login(self,username,password):
        """管理员/普通用户登陆"""
        self.sendkeys(username,*self.username_serach_loc)
        self.sendkeys(password,*self.password_search_loc)
        self.click(*self.login_button_search_loc)
        time.sleep(5)
        except_value1 = self.get_text(self.find_element(*self.uesrname_button_search_loc))
        unittest.TestCase().assertEqual(username, except_value1, username)
    def default_plate(self):
        """默认板块,删除帖子"""
        time.sleep(1)
        self.click(*self.default_plate_search_loc)
        time.sleep(1)
        self.click(*self.dagou_search_loc)
        self.click(*self.delete_button_search_loc)
        self.click(*self.sure_to_delete_button_search_loc)
    def admin_center(self,password):
        """管理中心"""
        time.sleep(5)
        self.click(*self.administration_center_search_loc)
        self.open_second_window()
        # time.sleep(5)
        self.sendkeys(password,*self.administration_center_password_search_loc)
        self.click(*self.submit_search_loc)
    def add_new_plate(self,platename):
        """添加新板块"""
        # self.open_second_window()
        time.sleep(5)
        self.click(*self.disciz_button_search_loc)
        time.sleep(3)
        self.switch_to_frame()
        self.click(*self.add_new_plate_search_loc)
        self.sendkeys(platename,*self.new_plate_name_search_loc)
        self.click(*self.new_plate_submit_search_loc)
        self.switch_to_frame_out()
        time.sleep(3)
        self.click(*self.new_plate_edit_search_loc)
        self.click(*self.logout_button_search_loc)           #管理员退出
    def new_plate(self):
        self.F5()
        self.click(*self.new_plate_search_loc)
    def fatie(self, title, content):
        self.sendkeys(title, *self.title_search_loc)
        self.sendkeys(content, *self.fatie_message_search_loc)
        self.click(*self.fatei_button_search_loc)
        time.sleep(5)
        except_value = self.get_text(self.find_element(*self.fatie_title_text_search_loc))
        unittest.TestCase().assertEqual(except_value,title,title)
    def huitie(self, content):
        time.sleep(5)
        self.click(*self.huitie_search_loc)
        self.sendkeys(content, *self.huitie_message_search_loc)
        self.click(*self.huitie_button_search_loc)