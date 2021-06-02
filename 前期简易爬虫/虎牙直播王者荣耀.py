# -*- coding: UTF-8 -*-
'''
@Project ：dict_sum.py 
@File    ：虎牙直播王者荣耀.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/6/2 13:28 
'''
from fake_useragent import UserAgent
from lxml import etree
import requests
headers = {
    'User-Agent':UserAgent().chrome
}
url = 'https://www.huya.com/g/wzry'
response = requests.get(url=url)
html = etree.HTML(response.text)
li_list = html.xpath('//*[@id="js-live-list"]/li')
for li in li_list:
    title = li.xpath('./a[2]/@title')[0] #直播标题
    name = li.xpath('./span/span[1]/img/@title')[0] #主播名
    number = li.xpath('./span/span[2]/i[2]/text()')[0].strip() #观众人数
    with open('虎牙王者荣耀.txt','a',encoding='UTF-8') as fp:
        fp.write(title+'\t'+name+"\t"+number+"\n")
        print(name,'已完成')

