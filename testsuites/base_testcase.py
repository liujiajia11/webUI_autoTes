import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine

logger=Logger(logger="BaseTestCase").getlog()

class BaseTestCase(unittest.TestCase):
    be=BrowserEngine()
    def setUp(self):
        self.be.open_browser()
        self.driver=self.be.driver

    def tearDown(self):
        self.be.quit_browser()