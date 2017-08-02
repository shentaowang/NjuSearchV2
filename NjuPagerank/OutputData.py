# -*- coding:utf-8 -*-
import pymongo #使用mongodb存储谷歌矩阵

connection = pymongo.MongoClient()
db = connection.njusearch
bulk = db.njumatrix
bulk.remove({})

class Outputpi(object):
    def OutputMongo(self, data):
        bulk.insert(data)

