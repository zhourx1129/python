from fake_useragent import UserAgent    
from lxml import etree
import requests
import os

# 判断是否存在此文件夹，如果没有则创建一个
path = './美女图片/'
if not os.path.exists(path):
    os.makedirs(path)
# ua伪装
headers = {
    'User-Agent': UserAgent().random
}
# 主页网址
# homePage_url = 'https://pic.netbian.com/4kmeinv/'
# response = requests.get(homePage_url,headers=headers)
# response.encoding = "GBK"
# html = etree.HTML(response.text)
# li_list = html.xpath('//ul[@class="clearfix"]/li')
# for li in li_list:
#     #获取图片名称
#     picture_name = li.xpath('./a/b/text()')[0] + 'jpg'
#     # 获取图片下载链接
#     picture_url = 'https://pic.netbian.com/' + li.xpath('./a/@href')[0]
#     down = requests.get(picture_url,headers).content
#     with open(path + picture_name, 'wb') as fp:
#         fp.write(down)
#         print(picture_name,"下载完毕!")
# print("over!")


# 设置保存路径
# path = r'D:\test\picture_1\ '
# 目标url
url = "http://pic.netbian.com/4kmeinv/index.html"
# 伪装请求头  防止被反爬
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Referer": "http://pic.netbian.com/4kmeinv/index.html"
}
# 发送请求  获取响应
response = requests.get(url, headers=headers)
# 打印网页源代码来看  乱码   重新设置编码解决编码问题
# 内容正常显示  便于之后提取数据
response.encoding = 'GBK'
html = etree.HTML(response.text)
# xpath定位提取想要的数据  得到图片链接和名称
img_src = html.xpath('//ul[@class="clearfix"]/li/a/img/@src')
# 列表推导式   得到真正的图片url
img_src = ['http://pic.netbian.com' + x for x in img_src]
img_alt = html.xpath('//ul[@class="clearfix"]/li/a/img/@alt')

for src, name in zip(img_src, img_alt):
    img_content = requests.get(src, headers=headers).content
    img_name = name + '.jpg'
    with open(path + img_name, 'wb') as f:   # 图片保存到本地
    	print(f"正在为您下载图片：{img_name}")
        f.write(img_content)