from framework.base import BasePage
from framework.logger import Logger
from selenium.webdriver.common.by import By
import time

logger=Logger(logger="TwoDiscuz").getlog()

class TwoDiscuz(BasePage):
        kuang_button_delete_loc=(By.NAME,'moderate[]')
        delete_button_delete_loc=(By.CSS_SELECTOR,'#mdly > p:nth-child(6) > strong:nth-child(1) > a')
        delete_sure_button_delete_loc=(By.NAME,'modsubmit')

        login_guanlizhongxin_input_loc=(By.NAME,'admin_password')
        login_submit_guanlizhongxin_button=(By.NAME,'submit')
        guanlizhongxin_button_bankuaiguanli_loc=(By.XPATH,'//*[@id="um"]/p[1]/a[6]')
        luntan_button_bankuaiguanli_loc=(By.ID,'header_forum')
        bankuaiguanli_button_bankuaiguanli_loc=(By.CSS_SELECTOR,'menu_forum > li:nth-child(1) > a')

        newbankuai_button_newbankuai_loc=(By.CSS_SELECTOR,'#cpform > table > tbody:nth-child(3) > tr > td:nth-child(2) > div > a')
        submit_button_newbankuai_loc=(By.ID,'submit_editsubmit')
        logout_button_newbankuai_loc=(By.CSS_SELECTOR,'#frameuinfo> p:nth-child(1) > a')

        logout_button_logout_loc = (By.CSS_SELECTOR, '#um > p:nth-child(2) > a:nth-child(18)')

        newfatie_button__newfatie_loc=(By.CSS_SELECTOR,'#category_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > h2 > a')

        # 删除帖子
        def delete(self):
            self.current_window_handle()
            time.sleep(3)
            self.click(*self.kuang_button_delete_loc)
            self.click(*self.delete_button_delete_loc)
            self.click(*self.delete_sure_button_delete_loc)

        # 进入版块管理(管理中心--论坛)
        def bankuaiguanli(self,pwd):
            self.current_window_handle()
            self.click(*self.guanlizhongxin_button_bankuaiguanli_loc)
            self.window_handle(1)
            self.sendkeys(pwd,*self.login_guanlizhongxin_input_loc)
            self.click(*self.login_submit_guanlizhongxin_button)

            self.current_window_handle()
            self.click(*self.luntan_button_bankuaiguanli_loc)
            # self.click(*self.bankuaiguanli_button_bankuaiguanli_loc)


        #  创建新的版块
        def newbankuai(self):
            self.current_window_handle()
            self.frame()
            self.click(*self.newbankuai_button_newbankuai_loc)
            self.click(*self.submit_button_newbankuai_loc)


         #管理员退出
        def logout(self):
            self.current_window_handle()
            self.click(*self.logout_button_newbankuai_loc)
            self.current_window_handle()
            self.click(*self.logout_button_logout_loc)


         # 普通用户登录
         #进入新的版块，发帖
        def newfatie(self):
            self.current_window_handle()
            self.click(*self.newfatie_button__newfatie_loc)

















