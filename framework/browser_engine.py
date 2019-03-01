import os
from selenium import webdriver
from framework.logger import Logger
from configparser import ConfigParser

logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine:
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+"/tools/IEDriverServer.exe"

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get("browserYype","browser")
        logger.info("You had select %s browser."%browser)

        url=config.get("testServer","URL")
        logger.info("The text url is %s"%url)

        if browser=="Firefox":
            logger.info("Starting Firefox browser.")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        self.driver.get(url)
        logger.info("Open url: %s"%url)
        self.driver.maximize_window()
        logger.info("Maximize the current window")
        self.driver.implicitly_wait(5)
        logger.info("Set implicitly wait 10 seconds.")
        return self.driver

    def quit_browser(self):
        logger.info("Now Close and quit the browser.")
        self.driver.quit()