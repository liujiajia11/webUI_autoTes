from framework.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger

ligger=Logger(logger="FourDiscuz").getlog()

class FourDiscuz(BasePage):
    fatie_button_newtie_loc=(By.ID,'newspecial')
    toupiao_button_newtie_loc=(By.CSS_SELECTOR,'#newspecial_menu > li.poll > a')
    title_input_newtie_loc=(By.NAME,'subject')
    body1_input_newtie_loc=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(1) > input')
    body2_input_newtie_loc=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(2) > input')
    body3_inout_newtie_loc=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(3) > input')
    submit_button_newtie_loc=(By.ID,'postsubmit')

    toupiao_button_toupiao_loc=(By.ID,'option_1')
    submit_button_toupiao_loc=(By.NAME,'pollsubmit')

    title_text_toupiaodata_loc=(By.ID,'thread_subject')
    data1_join_loc=(By.CSS_SELECTOR,'td.pvt label')
    data2_join_loc=(By.CSS_SELECTOR,'div.pcbs form  tr > td:nth-child(2)')


    # 发表投票帖子
    def newtie(self,title,body1,body2,body3):
        self.move_to_element(*self.fatie_button_newtie_loc)
        self.click(*self.toupiao_button_newtie_loc)
        self.current_window_handle()
        self.sendkeys(title,*self.title_input_newtie_loc)
        self.sendkeys(body1,*self.body1_input_newtie_loc)
        self.sendkeys(body2,*self.body2_input_newtie_loc)
        self.sendkeys(body3,*self.body3_inout_newtie_loc)
        self.click(*self.submit_button_newtie_loc)

    # 进行投票
    def toupiao(self):
        self.click(*self.toupiao_button_toupiao_loc)
        self.click(*self.submit_button_toupiao_loc)

    # 取出投票各个选项的名称以及投票比例,取出投票的主题名称
    def toupiaodata(self):
        self.current_window_handle()
        loc_title=self.find_element(*self.title_text_toupiaodata_loc)
        title=self.text(loc_title)
        print("投票的主题名称：",title)
        data1_list=self.find_elements(*self.data1_join_loc)
        data2_list=self.find_elements(*self.data2_join_loc)
        for i in range(0,len(data1_list)):
            print("选项的名称:",self.text(data1_list[i]),"投票比例",self.text(data2_list[i*2+1]))












