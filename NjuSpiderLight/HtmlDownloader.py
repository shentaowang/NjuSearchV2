# -*- coding:utf-8 -*-
import requests
import re
import csv


ReUrlFile = 'OutputUrl.csv'

class Downloader(object):
    def __init__(self):
        self.cafile = "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem"

    def StaticDownloadNoencode(self, url, id, fp_error): #Get the static content of the web page
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}

        if url is None:
            return None

        if re.match('(.*?)\.pdf', url): #处理.pdf,.ppt 这类网页
            return None

        try:
            html = requests.get(url, headers=headers, timeout=90, verify=self.cafile)# seconds Requests will wait
        except Exception as e:
            fp_error.write("location1"+"\t"+url+'\t\t'+str(e)+'\t'+"\n")
            with open(ReUrlFile, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([str(id), url])
            return None

        return html

    def StaticDownload(self, url, id, fp_error): #Get the static content of the web page
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}

        if url is None:
            return None

        if re.match('(.*?)\.pdf', url): #处理.pdf,.ppt 这类网页
            return None

        try:
            html = requests.get(url, headers=headers, timeout=90, verify=self.cafile)# seconds Requests will wait
        except Exception as e:
            fp_error.write("location1"+"\t"+url+'\t\t'+str(e)+'\t'+"\n")
            with open(ReUrlFile, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([str(id), url])
            return None

        if html.encoding == 'ISO-8859-1': #中英文网页的编码问题
            html_text = html.text
            html_text = html_text.decode("utf8").encode("ISO-8859-1")
        else:
            html_text = html.text

        return html_text

    def StaticDownloadOne(self, url, fp_error): #Get the static content of the web page
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}

        if url is None:
            return None

        if re.match('(.*?)\.pdf', url): #处理.pdf,.ppt 这类网页
            return None

        try:
            html = requests.get(url, headers=headers, timeout=60, verify=self.cafile)# seconds Requests will wait
        except Exception as e:
            fp_error.write("location1"+"\t"+url+'\t\t'+str(e)+'\t'+"\n")
            with open(ReUrlFile, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([str(id), url])
            return None

        if html.encoding == 'ISO-8859-1': #中英文网页的编码问题
            html_text = html.text
            html_text = html_text.decode("utf8").encode("ISO-8859-1")
        else:
            html_text = html.text

        return html_text

    def StaticRead(self, html_path):
        FpHtml = open(html_path,'r')
        html_text = FpHtml.read()
        return html_text
