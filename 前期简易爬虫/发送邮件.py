# -*- coding: utf-8 -*-

import smtplib   #用于发送邮件
from email.mime.text import MIMEText   #邮件正文
from email.utils import formatdate    #

'''
def mail(my_sender,my_pass,to_user,my_nick,to_nick,mail_msg):
    msg = MIMEText(mail_msg)
    #发送人昵称和邮箱账号
    msg['From'] = formatdate([my_nick,my_sender])
    #接收者昵称和邮箱
    msg['To'] = formatdate([to_nick,to_user])
    #发送的主题
    msg['Subject'] = '来自爸爸的一封信'
    #配置邮件服务器和端口
    server = smtplib.SMTP_SSL('smtp.qq.com',465)
    #模拟登录
    server.login(my_sender,my_pass)
    #邮件内容的发送
    server.sendmail(my_sender,[to_user],msg.as_string())
    #关闭连接通道

my_sender = 'zhourx_1129@qq.com'
my_pass = 'pidnbcbcvjqicahe'
to_user = ['z534418624@163.com']
my_nick = ' '
to_nick = '儿子'
mail_msg = """
        儿子，想爸爸没
"""

#开始准备发送
for index in range(len(to_user)):

    try:
        mail(my_sender,my_pass,to_user,my_nick,to_nick,mail_msg)
        print("发送成功")
    except:
        print("发送失败！")
'''


import yagmail
user = 'zhourx_1129@qq.com'   #发送人邮箱
password = 'pidnbcbcvjqicahe'  #授权码
host = 'smtp.qq.com'   #邮件服务器
# 连接服务器
# 用户名、授权码、服务器地址
yag_server = yagmail.SMTP(user,password,host)

# 发送对象列表
email_to = ['z534418624@163.com' ]
#主题
email_title = ''
#内容(内容里可以是文件、html……)
email_content = [
            "<h1 style='color:red'>一级标题</h1>",#可以是html语言
            '小惊喜.jpg',#可以是文件,以附件形式发送
            yagmail.inline('a.jpg'),# 这样的话,图片会内嵌到正文
            'hello world', #可以是普通文本
            ]
# 附件列表
email_attachments = ['./小惊喜.jpg' ]

# 发送邮件
try:
    yag_server.send(email_to, email_title, email_content, email_attachments)
    print("发送成功")
except:
    print("发送失败")