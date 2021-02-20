from pynput.keyboard import Key,Controller as key_el    #键盘控制
from pynput.mouse import Button,Controller as mouse_el  #鼠标控制
import time  #计时控制

def key_input(string):
    key = key_el()  #键盘获得控制权
    key.type(string)  #打印出轰炸的内容
    key.press(Key.enter)     #模拟按下回车键
    key.release(Key.enter)  #模拟松开回车键


def mouse_click():
    mouse=mouse_el()  #鼠标获得控制权
    mouse.press(Button.left)
    mouse.release(Button.left)


def send_message(number,string):
    mouse_click()
    time.sleep(2)
    for i in range(number):
        time.sleep(0.5)
        key_input(string)


if __name__=='__main__':
    num = int(input("轰炸次数"))
    str = input("轰炸内容")
    send_message(num,str)

