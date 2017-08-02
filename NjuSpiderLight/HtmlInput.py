# -*- coding:utf-8 -*-
from numpy import *
import csv


class InputUrl(object):
    def ReadUrl(self, file):
        CsvFile = open(file, 'rb')
        CsvReader = csv.reader(CsvFile)
        list = []
        for row in CsvReader:
            list.append(row[1])
        return list

    def ReadId(self, file):
        CsvFile = open(file, 'rb')
        CsvReader = csv.reader(CsvFile)
        list = []
        for row in CsvReader:
            list.append(row[0])
        return list

    def ReadLanguage(self, file):
        CsvFile = open(file, 'rb')
        CsvReader = csv.reader(CsvFile)
        list = []
        for row in CsvReader:
            list.append(row[2])
        return list
