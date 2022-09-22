#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datetime
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import re

#LINE notifyの設定を行う
url = "https://notify-api.line.me/api/notify"
access_token = 'TFYNm2OtVpn6glS64JK7e3AIQJ3Vw5Wsm8FYVCgTO1m'
headers = {'Authorization': 'Bearer ' + access_token}

#天気サイトから欲しい情報を取得する
url2 = "https://tenki.jp/forecast/3/16/4410/13111/"   #欲しい情報があるURLを指定
res = requests.get(url2)                              #上記URL情報を取得する
soup = BeautifulSoup(res.content, 'html.parser')      #取得した情報をhtmlで解析する

# 以下各種情報を取得
target ="気"
yokohama_all=soup.find("h2").text
idx=yokohama_all.find(target)
yokohama=yokohama_all[:idx+1]

target2 =")"
hiniti=soup.find(class_="left-style").text
idx=hiniti.find(target2)
ddd=hiniti[:idx+1]                 

telop = soup.find("p", class_="weather-telop").string

highlists = soup.find("dd",class_="high-temp temp")

lowlists = soup.find("dd",class_="low-temp temp")

ttt = soup.find(class_="rain-probability")

row=[]
for t in ttt:
    row.append(t)

# message変数に通知したい文を代入する　改行したい場合は "\n" とダブルクォテーションで囲う
message="\n\n" + yokohama + "\n\n" + ddd + "\n" + telop + "\n" + "最高　" + highlists.text + "\n" + "最低　" + lowlists.text + "\n"+ "---------" + "\n" +row[1].text +"\n" + "~6  : " + row[3].text + "\n" + "~12 : " + row[5].text +"\n" + "~18 : " + row[7].text +"\n" + "~24 : " + row[9].text

payload = {'message': message}
r = requests.post(url, headers=headers, params=payload,)


# In[ ]:




