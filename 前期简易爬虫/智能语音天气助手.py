import requests                                                                                                                                                                                                                                     
from lxml import etree
import pyttsx3

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52'}
url='https://www.tianqi.com/luan'
r=requests.get(url=url,headers=headers) 
data=etree.HTML( r.text)
# print(data)
weather_list=data.xpath('//dl [@class="weather_info"]//text()')
# print(weather_list) 
weather_text=''.join(weather_list)
weather_text=weather_text.replace( "[切换城市]",'')
print(weather_text)

#语音播报功能
weather=pyttsx3.init()
weather.say(weather_text)
weather.runAndWait()
