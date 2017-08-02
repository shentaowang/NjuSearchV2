import xlrd
import csv

excle_name = raw_input('input the full exlce name you want trans\n')
book = xlrd.open_workbook(excle_name)
try:
    table = book.sheets()[0]
except Exception as e:
    print e

csv_name = raw_input('input the full csv name you want write\n')
csv_file = open(csv_name,'w')
nrows = table.nrows
ncols = table.ncols
row_data = []

for i in range(nrows):
    row_data = table.row_values(i)
    row_data[0] = str(int(float(row_data[0])))
    spamwriter = csv.writer(csv_file, quotechar=',',quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(row_data)

csv_file.close()

