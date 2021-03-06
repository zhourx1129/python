import requests
from lxml import etree
from fake_useragent import UserAgent

ua=UserAgent()
headers={
    'User-Agent':ua.random
}

old_url = 'https://movie.douban.com/top250'
for i in range(10):
    url = old_url+'?start=%d&filter='%(i*25)
    # print(url)
    response = requests.get(url=url,headers=headers)
    html = etree.HTML(response.text)
    li_list = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for li in li_list:
        name = li.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
        with open('./python/前期简易爬虫/豆瓣top250.txt','a') as fp:
            fp.write(name)
            fp.write("\n")
print("over!")