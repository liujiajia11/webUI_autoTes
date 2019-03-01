from framework.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger

logger=Logger(logger="ThreeDiscuz").getlog()
class ThreeDiscuz(BasePage):
    sousuo_input_sousuo_loc=(By.CSS_SELECTOR,'#scbar_txt')
    sousuo_button_sousuo_loc=(By.ID,'scbar_btn')

    tie_title_sousuo_loc=(By.CSS_SELECTOR,'h3 a')

    tie_title_jointie_loc=(By.ID,'thread_subject')

    # 用户登录

    # 进行帖子搜索
    def sousuo(self,content):
        self.sendkeys(content,*self.sousuo_input_sousuo_loc)
        self.click(*self.sousuo_button_sousuo_loc)
        self.window_handle(1)
        self.current_window_handle()

    # 进入搜索的帖子
    # def jointie(self):
        self.click(*self.tie_title_sousuo_loc)
        self.window_handle(2)
        self.current_window_handle()
    # 验证帖子标题和期望的一致
        title_loc= self.find_element(*self.tie_title_jointie_loc)
        title=self.text(title_loc)
        assert content in title
        print("验证成功，帖子标题%s和期望值%s一致"%(title,content))




    # 用户退出
