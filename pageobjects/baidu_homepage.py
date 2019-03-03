from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

     page_home_input_search_loc=(By.ID,"kw")
     page_home_button_search_loc=(By.ID,"su")

     def search(self,content):
         self.sendkeys(content,*self.page_home_input_search_loc)
         self.click(*self.page_home_button_search_loc)