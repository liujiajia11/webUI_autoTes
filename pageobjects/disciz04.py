from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time
import unittest
class ForthDisciz(BasePage):
    username_serach_loc = (By.ID, "ls_username")
    password_search_loc = (By.ID, "ls_password")
    login_button_search_loc = (By.TAG_NAME, "em")
    uesrname_button_search_loc = (By.CSS_SELECTOR, ".vwmy a")
    default_plate_search_loc = (By.XPATH,"//tr[1]/td/h2/a")   # 默认板块
    fatie_button_search_loc=(By.CSS_SELECTOR,"#newspecial img")       #发帖按钮
    #发起投票帖子
    start_vote_search_loc=(By.CSS_SELECTOR,".bm .tb li:nth-child(2) a")
    title_text_search_loc=(By.CSS_SELECTOR,".pbt .z .px")     #投票标题
    choise3_text_search_loc=(By.CSS_SELECTOR,".mbm p:nth-child(1)  input")    #选择1
    choise2_text_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2)  input")  # 选择2
    choise1_text_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(3)  input")  # 选择3
    start_vote_button_search_loc=(By.XPATH,"//div/button/span")   #发起投票按钮
    fatie_title_text_search_loc = (By.CSS_SELECTOR, ".ts span")
    #进行投票
    vote_choice_search_loc=(By.CSS_SELECTOR,".pcht table tr:nth-child(1) td:nth-child(1) input")
    submit_button_search_loc=(By.XPATH,"//button/span")
    #取出投票各个选项的名称、投票比例及投票主题
    vote_name1_search_loc=(By.CSS_SELECTOR,".pcht table tr:nth-child(1) td:nth-child(1) label")
    vote_proportion1_search_loc = (By.CSS_SELECTOR, ".pcht table tr:nth-child(2) td:nth-child(2) ")
    vote_name2_search_loc = (By.CSS_SELECTOR, ".pcht table tr:nth-child(3) td:nth-child(1) label")
    vote_proportion2_search_loc = (By.CSS_SELECTOR, ".pcht table tr:nth-child(4) td:nth-child(2) ")
    vote_name3_search_loc = (By.CSS_SELECTOR, ".pcht table tr:nth-child(5) td:nth-child(1) label")
    vote_proportion3_search_loc = (By.CSS_SELECTOR, ".pcht table tr:nth-child(6) td:nth-child(2) ")
    vote_title_search_loc=(By.XPATH,"//h1/span")

    def login(self,username,password):
        self.sendkeys(username,*self.username_serach_loc)
        self.sendkeys(password,*self.password_search_loc)
        self.click(*self.login_button_search_loc)
        time.sleep(5)
        except_value1 = self.get_text(self.find_element(*self.uesrname_button_search_loc))
        unittest.TestCase().assertEqual(except_value1, username, username)
        self.click(*self.default_plate_search_loc)

    def fabiao_vote(self,title,choice1,choice2,choice3):
        """发表投票帖子"""
        time.sleep(2)
        self.click(*self.fatie_button_search_loc)
        time.sleep(2)
        self.click(*self.start_vote_search_loc)
        time.sleep(2)
        self.sendkeys(title,*self.title_text_search_loc)
        self.sendkeys(choice1,*self.choise1_text_search_loc)
        self.sendkeys(choice2, *self.choise2_text_search_loc)
        self.sendkeys(choice3, *self.choise3_text_search_loc)
        self.click(*self.start_vote_button_search_loc)
        time.sleep(2)
        except_value = self.get_text(self.find_element(*self.fatie_title_text_search_loc))
        unittest.TestCase().assertEqual(except_value,title,title)
    def take_note(self):
        """进行投票"""
        self.click(*self.vote_choice_search_loc)
        self.click(*self.submit_button_search_loc)
    def text(self):
        time.sleep(5)
        name1=self.find_element(*self.vote_name1_search_loc)
        name2 = self.find_element(*self.vote_name2_search_loc)
        name3 = self.find_element(*self.vote_name3_search_loc)
        proportion1 = self.find_element(*self.vote_proportion1_search_loc)
        proportion2=self.find_element(*self.vote_proportion2_search_loc)
        proportion3 = self.find_element(*self.vote_proportion3_search_loc)
        title=self.find_element(*self.vote_title_search_loc)
        print(self.get_text(name1),self.get_text(name2),self.get_text(name3))
        print(self.get_text(proportion1),self.get_text(proportion2),self.get_text(proportion3))
        print(self.get_text(title))

