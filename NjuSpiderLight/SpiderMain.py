# -*- coding:utf-8 -*-
import HtmlInput
import HtmlOutput
import HtmlDownloader
import HtmlDeal
import time
import re
from goose import Goose
from goose.text import StopWordsChinese
from pymongo import MongoClient

ErrorFile = "error.txt"#请手动清除
OutputFile = "result.json"
UrlFile = "id_url_langua.csv"
ReUrlFile = 'OutputUrl.csv'

model_list = [
"test small set of url(0)",
"test model(1)"
]
for model_item in model_list:
    print model_item

model_num = raw_input("Choose the model num:\n")
#model_num = 0

if int(model_num) == 0:#download the html_code and transform it
    start_time = time.time()
    InputUrl = HtmlInput.InputUrl()
    Downloader = HtmlDownloader.Downloader()
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()

    FpError = open(ErrorFile, 'a')
    FpError.write("The scipt is:SpiderMian.py\tThe model is:0\n")
    FpError.write("start:\t" + time.ctime() + "\n\n")
    FpOutput = open(OutputFile, 'w')

    id_list = InputUrl.ReadId(UrlFile)
    url_list = InputUrl.ReadUrl(UrlFile)
    language_list = InputUrl.ReadLanguage(UrlFile)

    num = len(url_list)

    for i in range(num):
        html_text = Downloader.StaticDownload(url_list[i], int(id_list[i]), FpError)
        print ("id:%s\t\turl:%s")%(id_list[i], url_list[i])

        if language_list[i] == "chinese":
            g = Goose({"stopwords_calss":StopWordsChinese})
            try:
                article = g.extract(url=url_list[i])
                content = article.cleaned_text
                title = article.title
            except Exception as e:
                FpError.write("can't extract it\n id:%s\t\tcontent:%s\n")(id_list[i]. url_list[i])
                FpError.write("ratio is:%f")%(ratio)
                content = ""
                title = ""

        elif language_list[i] == "english":
            g = Goose()
            try:
                article = g.extract(url=url_list[i])
                content = article.cleaned_text
                title = article.title
            except Exception as e:
                FpError.write("can't extract it\n id:%s\t\tcontent:%s\n")(id_list[i]. url_list[i])
                FpError.write("ratio is:%f")%(ratio)
                content = ""
                title = ""


        elif language_list[i] == "unknow":
            g = Goose()
            try:
                article = g.extract(url=url_list[i])
                content = article.cleaned_text
                title = article.title
            except Exception as e:
                FpError.write("can't extract it\n id:%s\t\tcontent:%s\n")(id_list[i]. url_list[i])
                FpError.write("ratio is:%f")%(ratio)
                content = ""
                title = ""
                print content

        elif language_list[i] == "nocontent":
            content = ""
            title = ""


        output_es = HtmlDeal.SimpleTrs(title, content, url_list[i])
        OutputContent.OutputEs(output_es, int(id_list[i]), FpOutput)
    
    stop_time = time.time()
    print ("use time:%f")%(stop_time-start_time)




if int(model_num) == 1:#use the database html_code and transform it
    start_time = time.time()
    fail_number = 0
    SimpleDeal = HtmlDeal.SimpleDeal()
    OutputContent = HtmlOutput.OutputContent()

    FpError = open(ErrorFile, 'a')
    FpError.write("The scipt is:SpiderMian.py\tThe model is:0\n")
    FpError.write("start:\t" + time.ctime() + "\n\n")
    FpOutput = open(OutputFile, 'w')

    client = MongoClient()
    db = client.nju_web_code
    collection = db.version3
    num = collection.find().count()

    for i in range(1, num+1):
        print i
        query = collection.find_one({"web_id":i})
        if query['language'] == "chinese":
            g = Goose({"stopwords_class":StopWordsChinese})
            if query['encode'] == 'ISO-8859-1':
                raw_html = query['html_code'].decode("utf-8").encode("ISO-8859-1")
            else:
                raw_html = query['html_code']
            try:
                a = g.extract(raw_html=raw_html)
                title = a.title
                content = a.cleaned_text
                if len(content) <3:
                    fail_number = fail_number + 1
            except Exception as e:
                FpError.write("can't extract it\n id:%d\t\tcontent:%s\n")%(i)       
                content = ""
                title = ""

        elif query['language'] == "english":
            g = Goose()
            if query['encode'] == 'ISO-8859-1':
                raw_html = query['html_code'].decode("utf-8").encode("ISO-8859-1")
            else:
                raw_html = query['html_code']
            try:
                a = g.extract(raw_html=raw_html)
                title = a.title
                content = a.cleaned_text
                if len(content) <3:
                    fail_number = fail_number + 1
            except Exception as e:
                FpError.write("can't extract it\n id:%d\t\tcontent:%s\n")%(query['web_id'])       
                content = ""
                title = ""

        elif query['language'] == 'unknow':
            g = Goose()
            raw_html = query['html_code']
            try:
                a = g.extract(raw_html=raw_html)
                title = a.title
                content = a.cleaned_text
                if len(content) <3:
                    fail_number = fail_number + 1
            except Exception as e:
                FpError.write("can't extract it\n id:%d\t\tcontent:%s\n")%(query['web_id'])       
                content = ""
                title = ""

        elif query['language'] == 'nocontent':
            content = ""
            title = ""

        output_es = HtmlDeal.SimpleTrs(title, content, query['web_id'])
        OutputContent.OutputEs(output_es, query['web_id'], FpOutput)
        #print content

    stop_time = time.time()
    print ("use time:%f")%(stop_time-start_time)
    print ("fail_number is:%d")%(fail_number)
