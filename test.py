from selenium import webdriver
import os
driver = webdriver.Chrome("/Users/lizg2018/PycharmProjects/pyauto/webdriver/others/chromedriver")
''''''
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file("/Users/lizg2018/PycharmProjects/pyauto/exceptionpictures/2018-7-21/1.png")
print(os.name)
