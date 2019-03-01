from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz01 import OneDiscuz
from pageobjects.discuz03 import ThreeDiscuz
import time
import unittest
from framework.logger import Logger
logger=Logger(logger="DiscuzThreeTest").getlog()
class DiscuzThreeTest(BaseTestCase):
    '''第三题'''
    def testdiscuz(self):
        od=OneDiscuz(self.driver)
        od.login("123456","123456")
        time.sleep(4)
        td=ThreeDiscuz(self.driver)
        td.sousuo("haotest")

if __name__=="__main__":
    unittest.main(verbosity=2)

