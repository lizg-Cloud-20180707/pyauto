# encoding = utf- 8

from action.PageAction import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
import time
import traceback

# 设置此次测试的环境编码为 utf-8

import sys
from imp import reload
reload(sys)
# python 3和2很大区别就是python本身改为默认用unicode编码。不需要下列语句设置
# sys.setdefaultencoding("utf-8")

# 可测试获取当前的默认编码
# sys.getdefaultencoding()

# 创建解析 Excel 对象

excelObj = ParseExcel()
print(dataFilePath)
# 将 Excel 数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)
print("testScript-->"+"通过名称获取 sheet 对象的名字:")
