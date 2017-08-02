# -*- coding:utf-8 -*-
import xlrd
from numpy import *
import csv

class InputMatrix(object):
    def ReadExcle(self, file, OffsetRow, OffsetCol):
        workbook = xlrd.open_workbook(file)
        table1 = workbook.sheets()[1]
        nrows = table1.nrows
        ncols = table1.ncols
        array = zeros((nrows - OffsetRow, ncols - OffsetCol), dtype=float)
        for i in range(OffsetRow, nrows):
            for j in range(OffsetCol, ncols):
                if table1.cell(i, j).value is None:
                    pass
                elif table1.cell(i, j).value == 1:
                    array[i - 2, j - 2] = 1
        return array

    def ReadCsv(self, file, OffsetRow, Offsetcol):
        CsvFile = open(file, 'rb')
        CsvReader = csv.reader(CsvFile)
        OffSetRowShaw = OffsetRow
        OffSetColShaw = Offsetcol   #控制偏移，需要不断检查
        array_i = 0
        array_j = 0 #插入数组中的位置
        num = 0 #开辟数组大小
        watcher = 0
        for row in CsvReader:
            num += 1
        array = zeros((num - OffsetRow, num - Offsetcol), dtype=float)

        CsvFile.close()
        CsvFile = open(file, 'rb')
        CsvReader = csv.reader(CsvFile)
        for row in CsvReader: #此处是略过首行和首列，由于CSV文件没有好的读出方法，较为笨重
            if OffSetRowShaw == 0:
                OffSetColShaw = Offsetcol
                for col in row:
                    if OffSetColShaw == 0:
                        if int(col) == 0:
                            array[array_i, array_j] = 0
                            array_j += 1
                        elif int(col) == 1:
                            array[array_i, array_j] = 1
                            array_j += 1
                    elif OffSetColShaw != 0:
                        # print OffSetColShaw
                        OffSetColShaw -= 1
                array_i += 1
                array_j = 0
            elif OffSetRowShaw != 0:
                OffSetRowShaw -= 1

        return array


class InputUrl(object):
    def ReadUrl(self,file):
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
