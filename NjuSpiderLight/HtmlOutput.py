# -*- coding:utf-8 -*-
import json
import sys
#import pylab as pl
reload(sys)
sys.setdefaultencoding("utf-8")
import os


class SimpleTrs(object):
	def __init__(self, title, content, url):
		self.title = title
		self.content = content
		self.url = url

class OutputContent(object):
	def __init__(self, limit_len=6, limit_ratio=0.06, limit_num=7, max_num=10):
		self.limit_len = limit_len
		self.limit_ratio = limit_ratio
		self.limit_num = limit_num
		self.max_num = max_num
	
	def OutputEs(self, content, id, FpOutput):
		json_data = {"create": {"_index": "njusearch3", "_type": "test1", "_id": id}}
		json_data = json.dumps(json_data)
		FpOutput.write(json_data)
		FpOutput.write("\n")
		FpOutput.write(json.dumps(content, default=lambda obj: obj.__dict__, ensure_ascii=False))  # 序列化输出
		FpOutput.write("\n")

	def OutputEsNew(self, out_pots, id, FpOutput):
		cal_num = 0
		record_ratio = []
		content =""
		num_pots = len(out_pots)#out_pots[0][0]==title, out_pots[0][1]==url
		for i in range(1, num_pots-1):
			num1 = out_pots[i+1][1] - out_pots[i][1]#求解斜率，作为分子
			num2 = out_pots[i+1][0] - out_pots[i][0]#作为分母
			record_ratio.append(1.0*num1/num2)

		for i in range(1, num_pots-2):
			if(abs(record_ratio[i]) <= self.limit_ratio and cal_num < self.max_num):
				cal_num += 1
			else:
				if(cal_num > self.limit_num):
					for j in range(i-cal_num, i):
						out_pots[j] = 0
					cal_num = 0
				else:
					cal_num = 0

		for pots in out_pots[1:]:
			if isinstance(pots,list):
				content = content+" "+pots[2]

		content = SimpleTrs(out_pots[0][0], content, out_pots[0][1])
		json_data = {"create": {"_index": "njusearch3", "_type": "test1", "_id": id}}
		json_data = json.dumps(json_data)
		FpOutput.write(json_data)
		FpOutput.write("\n")
		FpOutput.write(json.dumps(content, default=lambda obj: obj.__dict__, ensure_ascii=False))  # 序列化输出
		FpOutput.write("\n")


	def OutPlot(self, plot_pots):
		cal_num = 0
		x = []
		y = []
		record_ratio = []
		num_pots = len(plot_pots)
		# for pots in plot_pots:
		# 	if pots[1] > limit_len:
		# 		x.append(pots[0])
		# 		y.append(pots[1])
		for i in range(num_pots-1):
			num1 = plot_pots[i+1][1] - plot_pots[i][1]#求解斜率，作为分子
			num2 = plot_pots[i+1][0] - plot_pots[i][0]#作为分母
			record_ratio.append(1.0*num1/num2)
			print 1.0*num1/num2
			#print "\n"

		for i in range(num_pots-1):
			if(abs(record_ratio[i]) <= self.limit_ratio and cal_num < self.max_num):
				cal_num += 1
			else:
				if(cal_num > self.limit_num):
					for j in range(i-cal_num, i):
						plot_pots[j] = 0
					cal_num = 1
				else:
					cal_num = 1

		for pots in plot_pots:
			if isinstance(pots,list):
				x.append(pots[0])
				y.append(pots[1])
		pl.plot(x, y, 'o')
		pl.show()

	def TestSet(self, out_pots, id, FpOutput):
		father_path = "testset/"
		cal_num = 0
		record_ratio = []
		content =""
		num_pots = len(out_pots)#out_pots[0][0]==title, out_pots[0][1]==url
		for i in range(1, num_pots-1):
			num1 = out_pots[i+1][1] - out_pots[i][1]#求解斜率，作为分子
			num2 = out_pots[i+1][0] - out_pots[i][0]#作为分母
			record_ratio.append(1.0*num1/num2)

		for i in range(1, num_pots-2):
			if(abs(record_ratio[i]) <= self.limit_ratio and cal_num < self.max_num):
				cal_num += 1
			else:
				if(cal_num > self.limit_num):
					for j in range(i-cal_num, i):
						out_pots[j] = 0
					cal_num = 1
				else:
					cal_num = 1

		for pots in out_pots[1:]:
			if isinstance(pots,list):
				content = content+" "+pots[2]
		file_name = FpOutput + str(id)+ ".txt"
		OutFile = os.path.join(sys.path[0], "testset", file_name)
		FpOutput = open(OutFile,'w')
		FpOutput.write(json.dumps(content, default=lambda obj: obj.__dict__, ensure_ascii=False))  # 序列化输出
		FpOutput.write("\n")
		FpOutput.close()



