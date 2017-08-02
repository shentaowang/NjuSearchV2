# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import re
import requests
import sys
import os
from FileCompare import FileDiff

import urllib2

file = "test.txt"
url = "http://stuex.nju.edu.cn/a/liuxueshuominghui/20160311/1022.html"
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(url)
raw_html1 = response.read()


html = requests.get(url)# seconds Requests will wait
raw_html2 = html.text

fp = open(file, 'w')

fp.write(raw_html1)
fp.write("___________________________________")
fp.write(raw_html2)

#file1 = os.path.join(sys.path[0],folder,file1)
#file2 = os.path.join(sys.path[0],folder,file2)
#FileDiff().TwoFileCompare(file1,file2)

#FileDiff().TwoFileSimilarity(file1, file2)

#def test():
 #   print file1

#test()
# url = 'http://stuex.nju.edu.cn/'
# id = 1
# ErrorFile = "error.txt"
# FpError = open(ErrorFile, 'a')
#
#
# Downloader = HtmlDownloader.Downloader()
# SimpleDeal = HtmlDeal.SimpleDeal()
# OutputContent = HtmlOutput.OutputContent()
#
# html_text = Downloader.StaticDownload(url, FpError)
# html_text = html_text.decode("utf8").encode("ISO-8859-1")
# print html_text
# OutputS = SimpleDeal.Method1(url, html_text, None)
# OutputContent.OutputEs(OutputS, id, None)

# ContentTest = 'admin　\r\n             点击:首页'
# print ContentTest
# ContentTest = ContentTest.replace('\r\n', '')
# print ContentTest
# ContentTest = ContentTest.replace(' ', '', 50)
# print ContentTest

# TestUrl = 'http://stuex.nju.edu.cn/en/a/guide_for_students'
# TestId = 2933
# OutputFile = "test.json"
# ErrorFile = "Testerror.txt"
#
# FpOutput = open(OutputFile, 'w')
# FpError = open(ErrorFile, 'a')
# FpError.write("start:\t"+time.ctime()+"\n\n")
#
# Downloader = HtmlDownloader.Downloader()
# SimpleDeal = HtmlDeal.SimpleDeal()
# OutputContent = HtmlOutput.OutputContent()
#
# print ("id:%d \t\t url:%s") % (TestId, TestUrl)
# html_text = Downloader.StaticDownload(TestUrl, FpError)
# OutputS = SimpleDeal.Method1(TestUrl, html_text, FpError)
# OutputContent.OutputEs(OutputS, TestId, FpOutput)

# url = 'http://stuex.nju.edu.cn/uploads/soft/160929/3-160929203359.pdf'
# if re.match('(.*?)\.pdf', url):
#     print 'ok'



