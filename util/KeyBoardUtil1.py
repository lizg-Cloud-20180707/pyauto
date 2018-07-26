import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
"""
使用示例
//分别定义一个实例 
m = PyMouse() 
k = PyKeyboard()

鼠标操作： 
m.click(x,y,button,n) –鼠标点击 
x,y –是坐标位置 
buttong –1表示左键，2表示点击右键 
n –点击次数，默认是1次，2表示双击

m.move(x,y) –鼠标移动到坐标(x,y)

x_dim, y_dim = m.screen_size() –获得屏幕尺寸

键盘操作：

k.type_string(‘Hello, World!’) –模拟键盘输入字符串 
k.press_key(‘H’) –模拟键盘按H键 
k.release_key(‘H’) –模拟键盘松开H键 
k.tap_key(“H”) –模拟点击H键 
k.tap_key(‘H’,n=2,interval=5) –模拟点击H键，2次，每次间隔5秒 
k.tap_key(k.function_keys[5]) –点击功能键F5 
k.tap_key(k.numpad_keys[5],3) –点击小键盘5,3次

联合按键模拟 
例如同时按alt+tab键盘 
k.press_key(k.alt_key) –按住alt键 
k.tap_key(k.tab_key) –点击tab键 
k.release_key(k.alt_key) –松开alt键
"""
m = PyMouse() # 鼠标
k = PyKeyboard() # 键盘
class KeyboardKeys(object):
    '''模拟键盘按键类'''
    VK_CODE = {
        'enter':0x0D,
        'ctrl':0x11,
        'v':0x56
    }

    @staticmethod
    def keyDown(keyName):
        #按下按键
        #win32api.keybd_event(KeyboardKeys.VK_CODE[keyName],0,0,0)
        k.press_key(keyName)

    @staticmethod
    def keyUp(keyName):
        #释放按键
        #win32api.keybd_event(KeyboardKeys.VK_CODE[keyName],0,win32con,KEYEVENT_KEYUP,0)
        k.release_key(keyName)

    @staticmethod
    def oneKey(key):
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)

    @staticmethod
    def twoKeys(key1,key2):
        #模拟两个组合按键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key1)
        KeyboardKeys.keyUp(key1)
