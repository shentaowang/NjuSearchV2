# -*-coding:utf-8 -*-
import pymongo
import OutputData

# db = pymongo.MongoClient().bulk_example
# db = connection.njusearch1
# Matrix = db.njumatrix

# bulk = db.test
# bulk.find({}).remove()
# bulk.insert({'_id': 4})
# print db.test.count()
data = {"_id": 1}
outputer = OutputData.Outputpi()
outputer.OutputMongo(data)





