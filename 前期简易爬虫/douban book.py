# -*- coding: UTF-8 -*-
'''
@Project ：国家化妆品的selenium爬取.py 
@File    ：douban book.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/6/5 23:43 
'''
from lxml import etree
from fake_useragent import UserAgent
import requests

headers = {
    'User-Agent':UserAgent().random
}
url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
li_list = tree.xpath('//*[@id="subject_list"]/ul/li')
for li in li_list:
    detailed_information = li.xpath('./div[2]/div/text()')[0].strip()  #详细信息
    book_name = li.xpath('./div[2]/h2/a/text()')[0].strip()  #书名
    synopsis = li.xpath('./div[2]/p/text()')[0].strip()  #简介
    score = li.xpath('./div[2]/div/span[2]/text()')[0].strip() #评分
    with open('./豆瓣图书.txt','a',encoding='utf-8') as fp:
        fp.write(book_name+'\t'+score+'\t'+detailed_information+'\n'+'\t'+synopsis+'\n'+'\n')
        print(book_name,'已完成')
