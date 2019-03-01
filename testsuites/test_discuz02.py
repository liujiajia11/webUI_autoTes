from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz02 import TwoDiscuz
from pageobjects.discuz01 import OneDiscuz
import unittest
import time
from framework.logger import Logger

logger=Logger(logger="DiscuzTwoTest").getlog()
class DiscuzTwoTest(BaseTestCase):
    '''第二题'''
    def testDiscuz(self):
         od=OneDiscuz(self.driver)
         od.login("admin","admin")
         od.morenbankuai()

         td=TwoDiscuz(self.driver)
         td.delete()
         td.bankuaiguanli("admin")
         td.newbankuai()
         td.logout()

         od.login("123456","123456")
         time.sleep(3)
         td.newfatie()

         od.fatie("新帖2","新帖2的内容")
         od.huifu("新帖2的回复内容")

if __name__=="__main__":
    unittest.main(verbosity=2)