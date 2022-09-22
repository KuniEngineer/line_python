import requests
from bs4 import BeautifulSoup

#欲しい情報があるURLからHTML情報を取得する
url2 = httpstenki.jpforecast317461014100
res = requests.get(url2)
soup = BeautifulSoup(res.content, 'html.parser')

#以下で各情報を取得
hiduke = soup.find(class_=left-style).text
telop = soup.find(p, class_=weather-telop).text
highlists = soup.find(dd,class_=high-temp temp).text
lowlists = soup.find(dd,class_=low-temp temp).text