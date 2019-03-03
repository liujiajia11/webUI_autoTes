import unittest
from pageobjects.disciz04 import ForthDisciz
from testsuites.base_testcase import BaseTestCase
class DiscizSearch(BaseTestCase):
    def test_disciz_serach(self):
        fd=ForthDisciz(self.driver)
        fd.login("admin","111111")
        fd.fabiao_vote("你最喜欢吃的水果","草莓","哈密瓜","香蕉")
        fd.take_note()
        fd.text()

if __name__=="__main__":
    unittest.main()