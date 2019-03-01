from framework.base import BasePage
from framework.logger import Logger
from selenium.webdriver.common.by import By
import time
import unittest

logger=Logger(logger="OneDiscuz").getlog()

class OneDiscuz(BasePage):
    unittest_testcase=unittest.TestCase()

    name_input_login_loc=(By.ID,'ls_username')
    pwd_input_login_loc=(By.ID,'ls_password')
    login_button_login_loc=(By.CSS_SELECTOR,'tbody tr:nth-child(2) td:nth-child(3) button')
    assert_text_login_loc=(By.CSS_SELECTOR,'#um > p:nth-child(2) > strong > a')

    morenbankuai_button_morenbankuai_loc=(By.XPATH,'//*[@id="category_1"]/table/tbody/tr[1]/td[2]/h2/a')
    assert_text__morenbankuai_loc=(By.CSS_SELECTOR,'#ct > div > div.bm.bml.pbn > div > h1 > a')

    fatie_button_fatie_loc=(By.ID,'newspecial')
    title_input_fatie_loc=(By.NAME,'subject')
    body_input_fatie_loc=(By.CSS_SELECTOR,'body')
    fatie_submit_fatie_loc=(By.ID,'postsubmit')
    quickly_fatie_submit_fatie_loc=(By.CSS_SELECTOR,'#newspecial_menu > li:nth-child(1) > a')
    assert_text_fatie_loc=(By.ID,'thread_subject')

    huifu_input_huifu_loc=(By.ID,'fastpostmessage')
    huifu_submit_huifu_loc=(By.ID,'fastpostsubmit')
    assert_text_huifu_loc=(By.CSS_SELECTOR,'#postmessage_92')

    logout_button_logout_loc=(By.CSS_SELECTOR,'#um > p:nth-child(2) > a:nth-child(12)')

    def login(self,name,pwd):
        self.sendkeys(name,*self.name_input_login_loc)
        self.sendkeys(pwd,*self.pwd_input_login_loc)
        self.click(*self.login_button_login_loc)
        self.wait()
        self.current_window_handle()
        expect=self.text(self.find_element(*self.assert_text_login_loc))
        self.unittest_testcase.assertEqual(name,expect,msg=expect)


    def morenbankuai(self):
        time.sleep(3)
        morenbankuai_text=self.text(self.find_element(*self.morenbankuai_button_morenbankuai_loc))
        self.click(*self.morenbankuai_button_morenbankuai_loc)
        self.current_window_handle()
        expect=self.text(self.find_element(*self.assert_text__morenbankuai_loc))
        self.unittest_testcase.assertEqual(morenbankuai_text,expect,msg=expect)


    def fatie(self,fatie_title,fatie_body):
        self.move_to_element(*self.fatie_button_fatie_loc)
        self.click(*self.quickly_fatie_submit_fatie_loc)
        self.sendkeys(fatie_title,*self.title_input_fatie_loc)
        self.frame()
        self.sendkeys(fatie_body,*self.body_input_fatie_loc)
        self.current_window_handle()
        self.click(*self.fatie_submit_fatie_loc)
        self.wait()
        self.current_window_handle()
        expect=self.text(self.find_element(*self.assert_text_fatie_loc))
        self.unittest_testcase.assertEqual(fatie_title,expect,msg=expect)


    def huifu(self,huifu_body):
        self.current_window_handle()
        self.sendkeys(huifu_body,*self.huifu_input_huifu_loc)
        self.click(*self.huifu_submit_huifu_loc)
        # self.current_window_handle()
        expect=self.text(self.find_element(*self.assert_text_huifu_loc))
        self.unittest_testcase.assertEqual(huifu_body,expect,msg=expect)

    def logout(self):
        self.current_window_handle()
        self.click(*self.logout_button_logout_loc)
        self.wait()















