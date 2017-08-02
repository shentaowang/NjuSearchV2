#coding:utf-8
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
from FileCompare import FileDiff
import re

ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url_new.csv"
CsvFile = "id_url_langua.csv"
ReUrlFile = 'OutputUrl.csv'

InputUrl = HtmlInput.InputUrl()
Downloader = HtmlDownloader.Downloader()
SimpleDeal = HtmlDeal.SimpleDeal()

FpError = open(ErrorFile, 'a')
FpError.write("The script is:AddLanguage.py\n")
FpError.write("start:\t" + time.ctime() + "\n\n")
csv_file = open(CsvFile, 'w')

id_list = InputUrl.ReadId(UrlFile)
url_list = InputUrl.ReadUrl(UrlFile)
num = len(url_list)

spamwriter = csv.writer(csv_file, quotechar=',', quoting=csv.QUOTE_MINIMAL)

for i in range(num):
    row_data = []
    print ("id:%s\t\turl:%s")%(id_list[i],url_list[i])
    html_text = Downloader.StaticDownload(url_list[i], int(id_list[i]), FpError)
    row_data.append(id_list[i])
    row_data.append(url_list[i])
    if html_text == None:
        row_data.append("nocontent")
        spamwriter.writerow(row_data)
    else:
        content = SimpleDeal.DeleteLabel(html_text)
        re_chinese = re.findall(u'[\u4e00-\u9fa5]',content)
        re_english = re.findall("[A-Za-z]+", content)
        chinese_len = len(re_chinese)
        english_len = len(re_english)
        ratio = chinese_len*1.0/(chinese_len+english_len+1)
        if ratio > 0.8:
            row_data.append("chinese")
        elif ratio < 0.2:
            row_data.append("english")
        else:
            row_data.append("unknow")
        row_data.append(ratio)
        spamwriter.writerow(row_data)
