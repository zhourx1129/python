import requests
from lxml import etree
import os   #创建文件夹
url='https://music.163.com/discover/toplist?id=3778678'
head={
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
down_url='https://music.163.com/song/media/outer/url?id='
respone=requests.get(url,headers=head)
# print(respone)
html=etree.HTML(respone.text)
id_list=html.xpath('//a[contains(@href,"song?")]')
# print(id_list)
for id in id_list:
    href=id.xpath('./@href')[0]
    # print(href)
    music_id=href.split('=')[1]
    # print(music_id)
    if "$" not in music_id:
        music_name=id.xpath('./text()')[0]
        # print(music_name)
        music_url=down_url + music_id
        music=requests.get(url=music_url,headers=head)
        # print(music_url)
        if not os.path.exists(r'D:\网易云'):
            os.mkdir(r'D:\网易云')
        else:
            with open(r'D:\网易云/%s.mp3' % music_name, "wb") as f:
                print("正在下载歌曲 《%s》 ..." % music_name)
                f.write(music.content)