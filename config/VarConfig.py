# encoding = utf-8
import os
# 获取当前文件所在目录的父目录绝对路径

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


try:
    if os.name == "posix":
        ieDriverFilePath = ""
        chromeDriverFilePath = parentDirPath + "/webdriver/others/chromedriver"
        firefoxDriverFilePath = parentDirPath + "/webdriver/others/geckodriver"
        # 异常图片存放目录
        screenPicturesDir = parentDirPath + "/exceptionpictures/"
        # 测试数据文件存放绝对路径
        dataFilePath = parentDirPath + "/testdata/test.xlsx"
        # 日志存放路径
        logFilePath = parentDirPath + "/config/Logger.conf"
        #print("os" + dataFilePath)

    elif os.name == "nt":
        ieDriverFilePath = ""
        chromeDriverFilePath = parentDirPath +u"\\webdriver\\windows\\chromedriver.exe"
        firefoxDriverFilePath = parentDirPath + u"\\webdriver\\windows\\geckodriver.exe"
        # 异常图片存放目录
        screenPicturesDir = parentDirPath + u"\\exceptionpictures\\"
        # 测试数据文件存放绝对路径
        dataFilePath = parentDirPath + u"\\testdata\\test.xlsx"
         # 日志存放路径
        logFilePath = parentDirPath + u"\\config\\Logger.conf"

    else:
        print("Error: unknown system name!"+"\n")
        print("    Project will be closed")
        quit()
except Exception as e:
    raise e


# 测试数据文件中，测试用例表中部分列对应的数字序号（需要根据实际情况调整）
testCase_testCaseName = 1
testCase_frameWorkName = 3
testCase_testStepSheetName = 4
testCase_dataSourceSheetName = 5
testCase_isExecute = 6
testCase_runTime = 7
testCase_testResult = 8

# 用例步骤表中，部分列对应的数字序号

testStep_testStepDescribe = 1
testStep_keyWords = 2
testStep_locationType = 3
testStep_locatorExpression = 4
testStep_operateValue = 5
testStep_runTime = 6
testStep_testResult = 7
testStep_errorInfo = 8
testStep_errorPic = 9

# 数据源表中，是否执行列对应的数字编号，变量名称需要根据实际情况全局修改

dataSource_isExecute = 6
dataSource_email = 2
dataSource_runTime = 7
dataSource_result = 8
# 配置代理地址
# 无代理
#proxy_url ='--proxy-server='

# 曙光一
# proxy_url ='--proxy-server=http://100.67.76.9:10062'

# Agility NT12 环境二
# proxy_url ='--proxy-server=http://100.67.76.9:10082'

# 曙光三
# proxy_url = '--proxy-server=http://100.67.76.9:10003'

# Agility环境三超融合
# proxy_url = '--proxy-server=http://100.67.76.9:50301'

# 曙光五
# proxy_url = '--proxy-server=http://100.67.76.9:10005'

# 曙光六
# proxy_url = '--proxy-server=http://100.67.76.9:10006'

# 曙光九
# proxy_url = '--proxy-server=http://100.67.76.9:10042'

# 曙光十
# proxy_url = '--proxy-server=http://100.67.76.9:50101'

# 曙光十一
# proxy_url = '--proxy-server=http://100.67.76.9:10002'

# 曙光十二
proxy_url = '--proxy-server=http://100.67.154.166:51201'
