#!/usr/bin/env python
# coding: utf-8

# In[8]:


import datetime
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import re

#LINE notifyの設定を行う
url_line = "https://notify-api.line.me/api/notify"
access_token = 'pZ5AcvyZnjzUBOmadQk3Gk65rTPugWor5boGkJjEaB6'
headers = {'Authorization': 'Bearer ' + access_token}

#スケジュールのurlを取得する
url = "https://baseball.yahoo.co.jp/npb/teams/12/schedule"   #欲しい情報があるURLを指定
res = requests.get(url)                              #上記URL情報を取得する
soup = BeautifulSoup(res.content, 'html.parser')      #取得した情報をhtmlで解析する

#本日の日付を特定する
date = datetime.datetime.now()
month = date.month
day = date.day

#today_dateに合わせた情報を取得する
today_result = soup.find_all("div",class_="bb-calendarTable__wrap")[day+2].text.replace("\n","")

# message変数に通知したい文を代入する　改行したい場合は "\n" とダブルクォテーションで囲う
if today_result[int(len(str(day))):] =="試合なし":
    message="\n\n" + "本日{}月{}日の試合結果(速報)".format(month,day) + "\n\n" + today_result[int(len(str(day))):]
else:
    message="\n\n" + "本日{}月{}日の試合結果(速報)".format(month,day) + "\n\n" + "vs" + today_result[int(len(str(day))):]

payload = {'message': message}
r = requests.post(url_line, headers=headers, params=payload,)


# In[ ]:




