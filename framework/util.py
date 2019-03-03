import xlrd
from framework.logger import Logger

logger=Logger(logger="Util").getlog()
class Util():

    def read_excel(self,excelPath,sheetname="sheet1"):
        # 打开excel表
        workbook=xlrd.open_workbook(excelPath)
        # 打开对应的sheet
        sheet=workbook.sheet_by_name(sheetname)

        # 获取第一行，作为key
        keys=sheet.row_values(0)
        # 获取行数
        nrows=sheet.nrows
        # 获取列数
        ncols=sheet.ncols

        if nrows<=1:
            logger.error("此列表有且仅有一行数据。")
        else:
            r=[]
            # 控制行数
            for i in range(1,nrows):
                 sheet_data={ }
                 values=sheet.row_values(i)
                 # 控制列数
                 for j in range(ncols):
                     sheet_data[keys[j]]=values[j]
                 r.append(sheet_data)
        return r


