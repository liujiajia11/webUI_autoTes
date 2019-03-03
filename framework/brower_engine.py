import os.path
from selenium import webdriver
from framework.logger import Logger
from configparser import ConfigParser

logger=Logger(logger="BrowerseEngine").getlog()

class BrowerseEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrome_drive_path=dir+"/tools/chromedriver.exe"
    firefox_driver_path=dir+"/tools/geckodriver.exe"
    ie_driver_path = dir + "/tools/IEDriverServer.exe"

    def open_browers(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path)
        print(file_path)
        browers=config.get("browersType","browersname")
        logger.info("打开%s浏览器" %browers)
        url=config.get("testServer","url")
        logger.info("打开的url为：%s" %url)
        if browers=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_drive_path)
            logger.info("Starting Chrome browers")
        elif browers=="FireFox":
            # driver=webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting FireFox browers")
        elif browers=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browers")

        self.driver.get(url)
        logger.info("Open url:%s"%url)
        self.driver.maximize_window()
        logger.info("Maximize the current window")
        self.driver.implicitly_wait(5)
        logger.info("Set implicitly wait 10 seconds")
        return self.driver

    def quit_browers(self):
        logger.info("Now,close and quit the browers")
        self.driver.quit()

if __name__ == "__main__":
     d = BrowerseEngine().open_browers()