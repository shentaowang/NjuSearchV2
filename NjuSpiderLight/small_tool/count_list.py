#coding:utf-8
import csv
import re
import sys
import os


UrlFile = "id_url_new.csv"

#get the abspath for UrlFile
path = sys.path[0]
path_list = re.split("/", path)
depth = len(path_list)
file_path = "/"
for i in range(1, depth-1):
   print path_list[i]
   file_path = os.path.join(file_path,path_list[i])
file_path = os.path.join(file_path,UrlFile)

CsvFile = open(file_path, 'rb')
CsvReader = csv.reader(CsvFile)
num = 0
for row in CsvReader:
    list_taget = re.findall("list",row[1])
    if list_taget != []:
        num = num + 1
        print ("id:%s\t\turl:%s")%(row[0], row[1])
print num
