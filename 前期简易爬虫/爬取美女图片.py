from fake_useragent import UserAgent    
from lxml import etree
import requests
import os

#判断电脑是否存在此文件夹如果不存在就创建一个
path = r'D:\\美女图片\\'
if not os.path.exists(path):
    os.mkdir(path)

# ua伪装
headers = {
    'User-Agent': UserAgent().random
}

# 主页网址
homePage_url = 'https://pic.netbian.com/4kmeinv/'
response = requests.get(homePage_url,headers=headers)
#改变编码，防止乱码
response.encoding = "GBK"
#对网页进行解析
html = etree.HTML(response.text)
#获取图片的详细信息
li_list = html.xpath('//ul[@class="clearfix"]/li')
for li in li_list:
    #获取图片名称
    picture_name = li.xpath('./a/b/text()')[0] + '.jpg'
    # 获取图片下载链接
    picture_url = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
    # print(picture_name,picture_url)

    #准备保存
    down = requests.get(picture_url,headers).content
    with open(path + picture_name, 'wb') as fp:
        fp.write(down)
        print(picture_name,"下载完毕!")
        
print("over!")