from pynput.keyboard import Key,Listener

#用来记录键盘按下的内容
keyboard_text=''

#实现当监听到键盘按下之后的功能
def press(key):
    print("按下{}".format(key))
    global  keyboard_text   #定义全局变量
    keyboard_text += str(key) #保存键盘记录的内容
    # print(keyboard_text)


#松开之后的功能a
def release(key):
    # print("松开{}".format(key))
    with open('记录的内容.txt','w') as file:  #新建一个记事本
        file.write(keyboard_text)  #把监听获取到的内容写入记事本中

    #esc关闭程序
    if key == Key.esc:
        print("暂停程序")
        return False

#创建监听键盘的功能，关联相应的操作
with Listener(on_press=press,on_release=release) as listener:
    listener.join()   #创建按键监听的线程


