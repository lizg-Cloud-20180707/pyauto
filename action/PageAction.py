# encoding = utf-8
from selenium import webdriver
from config.VarConfig import ieDriverFilePath
from config.VarConfig import chromeDriverFilePath
from config.VarConfig import firefoxDriverFilePath
from util.ObjectMap import getElement
#from util.ClipboardUtil import Clipboard
#from util.KeyBoardUtil import KeyboardKeys
from util.DirAndTime import *
from util.WaitUtil import  WaitUtil
from selenium.webdriver.chrome.options import Options
import time


# 定义全局的 driver 变量
driver = None
# 全局的等待类实例对象
waitUtil = None

def open_browser(browserName, *arg):
    # 打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            # 创建 Chrome 浏览器的一个 Options 实例对象
            chrome_options = Options()
            chrome_options.add_argument('--proxy-server=http://100.67.154.166:51201')
            # 添加屏蔽 --ignore -certificate -errors 提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore - certificate -errors"])
            driver = webdriver.Chrome(
                executable_path = chromeDriverFilePath,
                chrome_options = chrome_options
            )
        else:
            driver = webdriver.Firefox()
        # driver 对象创建成功胡，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url,*arg):
    # 访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*arg):
    # 关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds, *arg):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*arg):
    # 清楚输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType, locatorExpression, inputContent):
    # 在页面输入框中输入数据
    global driver
    print("%s %s %s" %(locationType, locatorExpression, inputContent))
    try:
        getElement(driver,locationType,
                   locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*arg):
    # 单击页面元素
    global driver
    try:
        getElement(driver,locationType,locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesorce(assertString,*arg):
    # 断言页面源码是否存在某关键字或关键字符串
    try:
        assert assertString in driver.page_souece, \
            u"% s not found in page_source!" % assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as  e:
        raise e

def assert_title(titleStr,*arg):
    # 断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title, \
            u"% s not found in page_source!" % titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as  e:
        raise e

def getTitle(*arg):
    # 获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSorce(*arg):
    # 获取页面源码
    global driver
    try:
        return driver.page_souece
    except Exception as e:
        raise e

def switch_to_frame(locationType,frameLocatorExpression,*arg):
    # 切换进入 frame
    global driver
    try:
        driver.switch_to.frame(getElement
                               (driver,locationType,frameLocatorExpression))
    except Exception as e:
        raise e

def switch_to_default_content(*arg):
    # 切出 frame ,回到默认对话框中
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def paste_string(pasteString,*arg):
    # 模拟 Ctrl + V 操作
    try:
        Clipboard.setText(pasteString)
        # 等待 2 秒，防止代码执行得太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

def press_tab_key(*arg):
    # 模拟 Tab 键
    try : KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

def press_enter_key(*arg):
    # 模拟 Enter 键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    # 窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def capture_screen(*arg):
    # 截取屏幕图片
    global driver
    # 获取当期时间，精确到毫秒
    currTime = getCurrentTime()
    # 拼接异常图片保存的绝对路径及名称
    picNameAndPath = str(createCurrentDateDir())+"/"+str(currTime)+".png"
    try:
        # 截取屏幕图片，并保存为本地文件
        print(picNameAndPath)
        driver.get_screenshot_as_file(picNameAndPath)

    except Exception as e:
        raise e

def waitPresenceOfElementLocated(locationType,locatorExpression,*arg):
    ''' 显式等待页面元素出现在DOM中，但并不一定可见，
                            存在则返回该页面元素对象 '''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,*arg):
    ''' 检查 frame 是否存在，存在则切换进 frame 控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*arg):
    ''' 显式等待页面元素出现在DOM中，并且可见，存在则返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e


'''
open_browser("Chrome")
visit_url("https://cas.env12.shuguang.com/cas/login")


# In[6]:
sleep(5)
#waitFrameToBeAvailableAndSwitchToIt("xpath","//div[@class=\"form-title\"]/preceding::div")
input_string("id","username","admin")

'''





