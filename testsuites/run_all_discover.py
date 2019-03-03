import unittest
from testsuites.test_disciz01_serach import DiscuzSearch
from testsuites.test_disciz03_search import DiscizSearch

test_dir="./"
suite=unittest.TestLoader().discover(test_dir,pattern="test*.py")
#
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(DiscuzSearch))
# suite.addTest(unittest.makeSuite(DiscizSearch))

if __name__=="__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
