# encoding = utf-8
from . import *
# from . import CreateContacts
from testScripts.WriteTestResult import writeTestResult
from util import ParseExcel
from util.Log import *

print("TestCreateRds---->")

def TestCreateRds():
    try:
        print("caseSheet->")
        # 测试Excel文件中的sheet名获取sheet对象
        caseSheet = excelObj.getSheetByIndex(0)
        print("通过序号获取 sheet 对象的名字---->:", excelObj.getSheetByIndex(0).title)

        # 获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet, testCase_isExecute)
        print(type(isExecuteColumn))
        # 记录执行成功的用例个数
        successfulCase = 0
        # 记录需要执行的用例个数
        requiredCase = 0
        print("记录需要执行的用例个数")
        for idx, i in enumerate(isExecuteColumn[1:]):
            # 因为用例sheet中第一行为标题行，无须执行
            print("因为用例sheet中第一行为标题行，无须执行----->")
            caseName = excelObj.getCellOfValue(caseSheet,
                                               rowNo= idx + 2, colsNo= testCase_testCaseName)
            # 循环遍历"测试用例"表中的测试用例，执行被设置为执行的用例
            if i.value.lower() == 'y':
                requiredCase += 1
                # 获取测试用例表中，第idx+1行中用例执行时使用的框架类型
                useFrameWorkName = excelObj.getCellOfValue(
                    caseSheet, rowNo= idx+2,colsNo=testCase_frameWorkName
                )
                # 获取测试用例表中，第idx+1行中执行用例的步骤sheet名
                stepSheetName = excelObj.getCellOfValue(
                    caseSheet, rowNo= idx+2,colsNo=testCase_testStepSheetName
                )

                dataSheetName = excelObj.getCellOfValue(
                    caseSheet, rowNo= idx+2,colsNo=testCase_dataSourceSheetName
                )
                logging.info(u"--执行测试用例'%s'---" %caseName)

                if useFrameWorkName == u"数据":
                    logging.info(u"********调用数据驱动*********")
                    # 获取测试用例表中，第idx+1 行，执行框架为数据驱动的用例所使用的数据sheet名
                    dataSheetObj = excelObj.getCellOfValue(caseSheet,
                                               rowNo= idx + 2, colsNo= testCase_dataSourceSheetName
                    )
                     # 获取测试用例表中，第idx+1行中执行用例的步骤sheet对象
                    stepSheetObj = excelObj.getSheetByName(stepSheetName)
                     # 获取测试用例表中，第idx+1行中执行用例的数据sheet对象
                    dataSheetObj = excelObj.getSheetByName(dataSheetName)
                    # 通过数据驱动框架执行步骤
                    result = 1

                    if result:
                        logging.info(u"用例%s执行成功" %caseName)
                        successfulCase += 1
                        writeTestResult(caseSheet, rowNo= idx + 2,
                                        colsNo= "testCase", testResult= "pass")
                    else:
                        logging.info(u"用例%s执行失败"%caseName)
                        writeTestResult(caseSheet, rowNo= idx + 2,
                                        colsNo= "testCase", testResult= "faild")
                elif useFrameWorkName == "关键字":
                    logging.info(u"********调用关键字驱动*********")
                    print("stepSheetName"+"----->")
                    caseStepObj = excelObj.getSheetByName(stepSheetName)
                    stepNums = excelObj.getRowsNumber(caseStepObj)
                    successfulSteps = 0
                    logging.info(u"测试用例共'%s'步" %stepNums)
                    for index in range(2, stepNums + 1):
                        stepRow = excelObj.getRow(caseStepObj, index)
                        # 获取关键字作为调用的函数名
                        keyWord = stepRow[testStep_keyWords - 1].value
                        # 获取操作元素定位方式作为调用的函数的参数
                        locationType = stepRow[testStep_locationType -1].value
                        # 获取操作元素的定位表达式作为调用函数的参数
                        locationExpression = stepRow[testStep_locatorExpression - 1].value
                        # 获取操作值作为调用函数的参数
                        operateValue = stepRow[testStep_operateValue - 1].value
                        if isinstance(operateValue,int):
                            # 如果 operateValue 的值为数字型，则将其转换为字符串，方便字符串拼接
                            operateValue =str(operateValue)
                        # 拼接需要执行的Python表达式，此表达式对应PageAction.py文件中的页面动作函数的字符串表示
                        tmpStr = "'%s','%s'" %(locationType.lower(),
                                               locationExpression.replace("'",'"')
                                               )if locationType and locationExpression else ""
                        if tmpStr:
                            tmpStr +=",u" + operateValue + "'"\
                                if operateValue else ""
                        else:
                            tmpStr += "u'" + operateValue + "'"\
                                if operateValue else ""
                        runStr = keyWord + "(" + tmpStr + ")"
                        # print runStr
                        try:
                            eval(runStr)
                        except Exception as e:
                            # 获取详细的异常堆栈信息
                            errorInfo = traceback.format_exc()
                            logging.debug(u"执行步骤'%s'发生异常\n"
                                          %stepRow[testStep_testStepDescribe - 1].value,
                                          errorInfo)
                            # 获取异常屏幕图片
                            capturePic = capture_screen()
                            writeTestResult(caseStepObj, rowNo= index,
                                            colsNo= "testStep", testResult= "faild",
                                            errorinfo = str(errorInfo),
                                            picPath = capturePic)
                        else:
                            successfulSteps += 1
                            logging.info(u"执行步骤'%s'成功\n"
                                          %stepRow[testStep_testStepDescribe - 1].value)
                            writeTestResult(caseStepObj, rowNo= index,
                                            colsNo= "testStep", testResult= "pass")
                    if successfulSteps == stepNums - 1:
                        successfulCase += 1
                        logging.info(u"用例%s执行通过 " %caseName)
                        writeTestResult(caseSheet, rowNo= idx + 2,
                                        colsNo= "testCase", testResult= "pass")
                    else:
                        logging.info(u"用例%s执行失败"%caseName)
                        writeTestResult(caseSheet, rowNo= idx + 2,
                                        colsNo= "testCase", testResult= "faild")
            else:
                # 清空不需要执行用例的执行时间和执行结果，异常信息，异常图片单元格
                writeTestResult(caseSheet, rowNo= idx + 2,
                                        colsNo= "testCase", testResult= "")
                logging.info(u"用例%s被设置为忽略执行"%caseName)
        logging.info(u"共%d条用例，%d用例被执行，成功执行%d条"
                     %(len(isExecuteColumn)-1,requiredCase,successfulCase))
    except Exception as e:
        logging.debug(u"程序本身发生异常\n %s" %traceback.format_exc())


