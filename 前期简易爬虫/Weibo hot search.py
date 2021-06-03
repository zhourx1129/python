# -*- coding: UTF-8 -*-
'''
@Project ：dict_sum.py 
@File    ：Weibo hot search.py
@IDE     ：PyCharm 
@Author  ：zhourx
@Date    ：2021/6/3 13:23
'''
from fake_useragent import UserAgent
from lxml import etree
import requests
headers = {
    'User-Agent':UserAgent().random
}
url = 'https://s.weibo.com/top/summary?cate=realtimehot'

response = requests.get(url,headers).text
html = etree.HTML(response)
tr_list = html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')[1:]
for tr in tr_list:
    click_rate = tr.xpath('./td[2]/span/text()')  # 点击率
    if click_rate == []:
        continue
    else:
        title = tr.xpath('./td[2]/a/text()')[0] #热搜标题
        click_rate = tr.xpath('./td[2]/span/text()')[0]  # 点击率
        with open('微博热搜排行榜.txt','a',encoding='utf-8') as fp:
            fp.write(title+click_rate+'\n')
            print(title,'已完成')


