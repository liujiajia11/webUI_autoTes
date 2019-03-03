from testsuites.base_testcase import BaseTestCase
from pageobjects.disciz01 import FristDisciz
import unittest


class DiscuzSearch(BaseTestCase):
    def test_discuz_search(self):
        fd=FristDisciz(self.driver)
        fd.login("admin","111111")
        fd.default_plate()
        fd.fatie("city","北京，上海，西安")
        fd.huitie("想去")
        fd.logout()

if __name__=="__main__":
    unittest.main()