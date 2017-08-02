# coding=utf-8
from pymongo import MongoClient
import datetime
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import os
import csv
import sys
import json
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ErrorFile = "error.txt"#请手动清除
UrlFile = "id_url_new.csv"
ReUrlFile = 'OutputUrl.csv'

InputUrl = HtmlInput.InputUrl()
Downloader = HtmlDownloader.Downloader()
SimpleDeal = HtmlDeal.SimpleDeal()

FpError = open(ErrorFile, 'a')
FpError.write("The script is:HtmlCode.py\n")
FpError.write("start:\t" + time.ctime() + "\n\n")
client = MongoClient()
db = client.nju_web_code
#db.drop_collection('version1')
collection = db.version5

web_id = 0
language = "unkonw"
language_ratio = 0.2
try_number = 1
update_time = datetime.datetime.utcnow()
html_code = "just test"
encoding = "utf-8"
url = "unknow"

id_list = InputUrl.ReadId(UrlFile)
url_list = InputUrl.ReadUrl(UrlFile)
num = len(url_list)


for i in range(num):
    row_data = []
    print ("id:%s\t\turl:%s")%(id_list[i],url_list[i])
    html = Downloader.StaticDownloadNoencode(url_list[i], int(id_list[i]), FpError)
    if html == None:
        encoding = "nocontent"
        html_text = None
    else:
        encoding = html.encoding
        html_text = html.text
    web_id = int(id_list[i])
    url = url_list[i]

    if type(html_text) == type("str"):
        print "ok"
        html_text = html_text.decode('utf-8')

    if html_text == None:
        html_code = "nocontent"
        language = "nocontent"
    else:
        html_code = html_text
        if encoding == 'ISO-8859-1':#for encoding problem
            html_text = html.text
            html_text = html_text.decode('utf-8').encode('ISO-8859-1')
        content = SimpleDeal.DeleteLabel(html_text)
        re_chinese = re.findall(u'[\u4e00-\u9fa5]',content)
        re_english = re.findall("[A-Za-z]+", content)
        chinese_len = len(re_chinese)
        english_len = len(re_english)
        ratio = chinese_len*1.0/(chinese_len+english_len+1)
        if ratio > 0.8:
            language = "chinese"
        elif ratio < 0.2:
            language = "english"
        else:
            language = "unknow"

    update_time = datetime.datetime.utcnow()
    post = {"web_id" :web_id,
            "url":url,
            "language":language,
            "try_number":try_number,
            "update_time":update_time,
            "html_code":html_code,
            "encode":encoding
         }
    collection.insert_one(post)

print collection.count()
