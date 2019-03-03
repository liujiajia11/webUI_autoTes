import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.disciz03 import ThirdDisciz
class DiscizSearch(BaseTestCase,unittest.TestCase):
    def test_disciz_search(self):
        td=ThirdDisciz(self.driver)
        td.login("admin","111111")
        result=td.search_post("haotest")
        self.assertEqual(result,result,result)
        td.logout()


if __name__=="__mian__":
    unittest.main()