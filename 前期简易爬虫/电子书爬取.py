# -*- coding: UTF-8 -*-
'''
@Project ：国家化妆品的selenium爬取.py 
@File    ：电子书爬取.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/6/6 15:03 
'''
from lxml import etree
import requests
from fake_useragent import UserAgent
import os

headers = {
    'User-Agent':UserAgent().chrome,
}
# 详细信息页面 的网址
url = 'https://www.aixiaxs.com/book/'
# 输入书名其实是为了创建一个文件夹来存放 并无实际意义
book_name = input('请输入书名:>')
# 准备创建文件夹
dir_file = 'D://%s//'%book_name
if not os.path.exists(dir_file):
    os.mkdir(dir_file)
# 书本 id 为书的唯一凭证
id = input('请输入书本id:>')
# 对 url 进行拼接
url = url + id + '/'

response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
# 章节
li_list = tree.xpath('//*[@id="readerlist"]/ul/li')
for li in li_list:
    title = li.xpath('./a/@title')[0]
    href = 'https://www.aixiaxs.com/' + li.xpath('./a/@href')[0]
    detail = requests.get(href,headers)
    detail.encoding = 'utf-8'
    tree = etree.HTML(detail.text)
    content = tree.xpath('//*[@id="content"]/text()')
    for i in content:
        with open(dir_file+title+'.txt','a',encoding='utf-8') as fp:
            fp.write(i)
            print(title,'已完成')
