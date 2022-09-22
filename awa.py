#!/usr/bin/env python
# coding: utf-8

# In[30]:


import datetime
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import re

#LINE notifyの設定を行う
url_line = "https://notify-api.line.me/api/notify"
access_token = '9lvMgMXQBIA5T7bqtmziL9evLASJ6zZng4aHZ8Wcb7V'
headers = {'Authorization': 'Bearer ' + access_token}

#総武線運行情報
url_soubu = "https://transit.yahoo.co.jp/diainfo/61/0"   #欲しい情報があるURLを指定
res = requests.get(url_soubu)                              #上記URL情報を取得する
soup_soubu = BeautifulSoup(res.content, 'html.parser')      #取得した情報をhtmlで解析する

#浅草線運行情報
url_asakusa = "https://transit.yahoo.co.jp/diainfo/128/0"   #欲しい情報があるURLを指定
res = requests.get(url_asakusa)                              #上記URL情報を取得する
soup_asakusa = BeautifulSoup(res.content, 'html.parser')      #取得した情報をhtmlで解析する

# 総武線情報
target_name_soubu = "総"
ori_soubu = soup_soubu.find("h1").text
idx_soubu = ori_soubu.find(target_name_soubu)
line_name_soubu = ori_soubu[idx_soubu:] 

unkou_soubu = soup_soubu.find("dt").text

info_soubu = soup_soubu.find("dd").text

# 浅草線情報
target_name_asakusa = "都"
ori_asakusa = soup_asakusa.find("h1").text
idx_asakusa = ori_asakusa.find(target_name_asakusa)
line_name_asakusa = ori_asakusa[idx_asakusa:] 

unkou_asakusa = soup_asakusa.find("dt").text

info_asakusa = soup_asakusa.find("dd").text

# message変数に通知したい文を代入する　改行したい場合は "\n" とダブルクォテーションで囲う
message="\n\n" + line_name_soubu + "\n" + unkou_soubu + "\n" + info_soubu + "\n\n" + line_name_asakusa + "\n" + unkou_asakusa + "\n" + info_asakusa

payload = {'message': message}
r = requests.post(url_line, headers=headers, params=payload,)


# In[ ]:




