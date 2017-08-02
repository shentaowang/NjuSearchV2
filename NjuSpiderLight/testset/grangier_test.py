#coding:utf-8
import csv
from goose import Goose
from goose.text import StopWordsChinese
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import FileCompare


file_csv = "nju.csv"
file_out = "grangier"


CsvFile = open(file_csv, 'rb')
CsvReader = csv.reader(CsvFile)
g = Goose({"stopwords_class":StopWordsChinese})
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
FileDiff = FileCompare.FileDiff()


cursor = 1
for row in CsvReader:
    url = row[1]
    response = opener.open(url)
    raw_html = response.read()
    a = g.extract(raw_html=raw_html)
    file_out_path = os.path.join(sys.path[0],file_out+str(cursor)+".txt")
    file_compare_path = os.path.join(sys.path[0],str(cursor)+'.txt')
    fp = open(file_out_path, "w")
    fp.write(a.cleaned_text)
    fp.close()
    similarity = FileDiff.TwoFileSimilarity(file_out_path,file_compare_path)
    print ("the similarity of test:%d\t%f")%(cursor,similarity)
    cursor = cursor + 1


