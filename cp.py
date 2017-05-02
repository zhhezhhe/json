# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import shutil
sougou_list = 'sougou_list.txt'
def move_(filename,folder):
	
	if not os.path.isfile(filename):
		return "file not exists"

	if not os.path.exists(folder):
		os.mkdir(folder)

	shutil.copyfile(filename,folder+"/"+filename.split("/")[-1])
	return "file moved"

with open(sougou_list,'r') as reader:
    lines = reader.readlines()
    for line in lines:
    	# print(line.split('\n')[0])
    	filename = line.split('\n')[0].split(' ')[0]
    	folder = '/media/zh/E/sougou_shaixuan/' + line.split('\n')[0].split(' ')[1]
    	result = move_(filename,folder)
