# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import json
import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



class SimpleTrs(object):
    def __init__(self, title, content, url):
        self.title = title
        self.content = content
        self.url = url



class SimpleDeal(object):
    def DeleteLabel(self, html_text):
        soup = BeautifulSoup(html_text, "lxml")
        script = soup.find_all("script")  # 找到所有script的标签
        for x in script:  # 判断script标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        style = soup.find_all("style")  # 找到所有script的标签
        for x in style:  # 判断style标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        content = "\t".join(soup.stripped_strings)
        return content


    def Method1(self, url, html_text, fp_error):#简单地提取网页的信息
        if html_text is None:
            OutputS = SimpleTrs(None, None, url)
            return OutputS

        # html_text = html_text.replace('&nbsp;', '') #处理源码中不需要的字符
        # html_text = html_text.replace('\s*', ',')
        # html_text = html_text.replace('&emsp;', ',')

        soup = BeautifulSoup(html_text, "lxml")
        script = soup.find_all("script")  # 找到所有script的标签
        for x in script:  # 判断script标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        style = soup.find_all("style")  # 找到所有script的标签
        for x in style:  # 判断style标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        try:
            title = soup.title.string.strip()
        except Exception as e:
            fp_error.write("location2"+"\t"+url + '\t' + str(e) + '\t' + "\n")  # 出现读出title为空的情况，不太明白
            title = "None"

        content = "\t".join(soup.stripped_strings)
        OutputS = SimpleTrs(title, content, url)
        return OutputS


    def Method2(self, url, html_text, fp_error):#画图
        fp_record = open('record.txt','w')
        start = 0;
        num = 0;
        plot_pots = []

        html_text = html_text.replace('&nbsp;', '') #处理源码中不需要的字符
        html_text = html_text.replace('\s*', ',')
        html_text = html_text.replace('&emsp;', ',')
        soup = BeautifulSoup(html_text, "lxml")
        script = soup.find_all("script")  # 找到所有script的标签
        for x in script:  # 判断script标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        style = soup.find_all("style")  # 找到所有script的标签
        for x in style:  # 判断style标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")

        #fp_record.write(html_text)
        fp_record.write("\n--------------------------------------\n")
        for string in soup.stripped_strings:
            try:
                index = html_text.find(string, start)
            except Exception as e:
                fp_error.write("location3:"+str(e)+"\t"+string+"\n")
                continue

            if index == -1:
                 # 出现读出index无法找到
                fp_error.write("location3:"+"not found index:"+url+"\t"+string+"\n")
            else:
                string_len = len(string)
                start = index + string_len;
                num+=1
                plot_pots.append([index, string_len])
                #fp_record.write("num is:"+str(num)+"\n")
                #fp_record.write("position is:"+str(index)+"\n")
                #fp_record.write(string)
                #fp_record.write("\n")

        return plot_pots


    def Method3(self, url, html_text, fp_error):#简单地提取网页的信息
        out_pots = []
        start = 0
        # html_text = html_text.replace('&nbsp;', '') #处理源码中不需要的字符
        # html_text = html_text.replace('\s*', ',')
        # html_text = html_text.replace('&emsp;', ',')
        html_parser = HTMLParser.HTMLParser()
        html_text = html_parser.unescape(html_text)

        soup = BeautifulSoup(html_text, "lxml")
        script = soup.find_all("script")  # 找到所有script的标签
        for x in script:  # 判断script标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")
                
        style = soup.find_all("style")  # 找到所有script的标签
        for x in style:  # 判断style标签是否包含文本，若有，直接置为空
            if x.string != None:
                x.string.replace_with(" ")



        try:
            title = soup.title.string.strip()
        except Exception as e:
            fp_error.write("location4"+"\t"+url + '\t' + str(e) + '\t' + "\n")  # 出现读出title为空的情况，不太明白
            title = "None"
        out_pots.append([title, url])

        for string in soup.stripped_strings:
            try:
                index = html_text.find(string, start)
            except Exception as e:
                fp_error.write("location3:"+str(e)+"\t"+string+"\n")
                continue

            if index == -1:
                 # 出现读出index无法找到
                fp_error.write("location4:"+"not found index:"+url+"\t"+string+"\n")
            else:
                string_len = len(string)
                start = index + string_len;
                out_pots.append([index, string_len, string])

        return out_pots

