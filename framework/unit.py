import xlrd
import os
from framework.logger import Logger
logger=Logger(logger="Unit").getlog()
class Unit():
    def readdata(self,ecxel_path,sheetName="Sheet1"):
         workbiao=xlrd.open_workbook(ecxel_path)
         sheet=workbiao.sheet_by_name(sheetName)
         key=sheet.row_values(0)
         rowNum=sheet.nrows
         colNum=sheet.ncols
         if rowNum<=1:
             logger.info("excel中的数据小于或等于1行")
         else:
             r=[]
             for i in range(1,rowNum):
                 sheey_data={ }
                 value=sheet.row_values(i)
                 for j in range(0,colNum):
                     sheey_data[key[j]]=value[j]
                 r.append(sheey_data)
         return r
if __name__=="__main__":
    print(Unit().readdata(os.path.dirname(os.path.abspath("."))+"/data/info.xlsx"))