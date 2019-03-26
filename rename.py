# coding=utf-8
import os
import json
from collections import OrderedDict
# import sys
# sys.setdefaultencoding("utf-8")

names = ['antique','jazz','ballad','soft','rap','rock']
result=OrderedDict()
for name in names:
    #result中的元素也是一个字典的形式
    result[name]={}  #定义嵌套字典
for name in names:
	count = 1
	path='./origin_mp3_data/'+name+'/'
	files = os.listdir(path)

	for file in files:
		print(file)
		os.rename(os.path.join(path,file),os.path.join(path,name+'_'+str(count).zfill(4)+os.path.splitext(file)[1]))
		result[name][name+'_'+str(count).zfill(4)+os.path.splitext(file)[1]]=file
		count = count + 1

json_str = json.dumps(result, indent=4, ensure_ascii=False)
with open('result.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)
