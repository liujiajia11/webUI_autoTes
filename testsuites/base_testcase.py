import unittest
from framework.brower_engine import BrowerseEngine

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser=BrowerseEngine()
        self.driver = browser.open_browers()
        print("baseTestcase driver",self.driver)
        # self.driver=self.be.driver
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        # self.driver.get("http://www.baidu.com")
    def tearDown(self):
        self.driver.quit()
        # self.be.quit_browers()
         # self.be.quit_browers()