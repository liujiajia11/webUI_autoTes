from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz01 import OneDiscuz
from pageobjects.discuz04 import FourDiscuz
import unittest
from framework.logger import Logger

logger=Logger(logger="DiscuzFourTest").getlog()
class DiscuzFourTest(BaseTestCase):
    '''第四题'''
    def testdiscuz(self):
        od=OneDiscuz(self.driver)
        od.login("123456","123456")
        od.morenbankuai()

        fd=FourDiscuz(self.driver)
        fd.newtie("学习","python","软件测试","UI自动化测试")
        fd.toupiao()
        fd.toupiaodata()
if __name__=="__main__":
    unittest.main(verbosity=2)