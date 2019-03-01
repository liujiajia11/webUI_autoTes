import logging
import time
import os.path
class Logger:
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 输出到日志文件，设置
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+"/logs/"
        log_name=log_path+rq+'.log'
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
        # 定义输出格式
        formatter =logging.Formatter('%(asctime)s - %(name)s -%(levelname)s -%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
    def getlog(self):
        return self.logger

