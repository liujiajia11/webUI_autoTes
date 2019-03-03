import unittest
from pageobjects.disciz02 import SecondDisciz
from testsuites.base_testcase import BaseTestCase
class DiscizSearch(BaseTestCase):
    def test_disciz_search(self):
         sd=SecondDisciz(self.driver)
         sd.login("admin","111111")      #管理员登陆
         sd.default_plate()                #默认论坛，删除帖子
         sd.admin_center("111111")        #管理中心
         sd.add_new_plate("star")         #创建新板块
         sd.login("liujiajia","666666")  #普通用户登陆
         sd.new_plate()
         sd.fatie("Let's go","I went to Beijing")
         sd.huitie("welcome")
        
if __name__=="__mian__":
     unittest.main()

