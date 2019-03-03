import logging
import os.path
import time

class Logger():

    def __init__(self,logger):
        #创建一个logger对象
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  #日志输出的级别

        log_path=os.path.dirname(os.path.abspath("."))+"/logs/"
        nf=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))       #当前日期
        log_name=log_path+nf+".log"
        fh=logging.FileHandler(log_name)          #日志输出到文件
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()  # 日志输出到控制台
        self.logger.addHandler(ch)

        #日志输出格式
        self.formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        ch.setFormatter(self.formatter)
        fh.setFormatter(self.formatter)
    def getlog(self):
        return self.logger