#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json

source_file = "jw_content.4.json"
output_file = "result.json"
collection = "xssc4"
test = "test1"

f = open(source_file, 'r')
out_file = open(output_file,'w')

for i in f.readlines():
    data = json.loads(i)
    print data['num']
    command = {"create": {"_index": collection, "_type": test, "_id": int(data['num'])}}
    command_data = json.dumps(command)
    out_file.write(command_data)
    out_file.write('\n')
    data = json.dumps(data, ensure_ascii=False)
    out_file.write(data)
    out_file.write('\n')

f.close()
out_file.close()
