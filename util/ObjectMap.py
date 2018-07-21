# encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 3).until \
            (lambda x: x.find_element(by=locateType, value=locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 3).until \
            (lambda x: x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e

'''
if __name__ == '__main__':
    from selenium import webdriver

    # 进行单元测试
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    # 打印页面对象的标签名
    print(searchBox.tag_name)
#   driver.find_element_by_xpath('//form[@id="form"]//input[@id="kw"]').send_keys('heel')
    # 打印页面对象的标签名
    aList = getElements(driver,"tag name","a")
    print(len(aList))
    driver.quit()
    driver.find_element_by_xpath().send_keys()
'''
