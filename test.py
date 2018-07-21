from selenium import webdriver
import time
import os
driver = webdriver.Chrome()


chrome_options = webdriver.ChromeOptions()




chrome_options.add_argument('--proxy-server=http://100.67.154.166:51201')




driver = webdriver.Chrome(chrome_options=chrome_options)
''''''
#driver.get("http://www.baidu.com")
#driver.get_screenshot_as_file("/Users/lizg2018/PycharmProjects/pyauto/exceptionpictures/2018-7-21/1.png")
#print(os.name)
driver.get("https://cas.env12.shuguang.com/cas/login?service=https%3A%2F%2Fmanage.env12.shuguang.com%2Fmanage%2Flogin%2Fcas")
print("登录前："+driver.title)

time.sleep(3)
driver.find_element_by_id("username").send_keys("admin")


# In[8]:


driver.find_element_by_id("password").send_keys("Admin123")


# In[9]:


driver.find_element_by_xpath('//input[@value="登录"]').click()
time.sleep(5)
print("登录后"+driver.title)
