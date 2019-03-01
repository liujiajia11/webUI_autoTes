from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz01 import OneDiscuz
import time
from framework.logger import Logger
import unittest

logger=Logger(logger="DiscuzOne").getlog()
class DiscuzOneTest(BaseTestCase):
      '''第一题'''
      def testdiscuz(self):
          homepage=OneDiscuz(self.driver)
          homepage.login("123456","123456")
          homepage.morenbankuai()
          homepage.fatie("新帖1","新帖的内容")
          time.sleep(16)
          homepage.huifu("回复新帖1内容....")
          homepage.logout()
if __name__=="__main__":
    unittest.main(verbosity=2)