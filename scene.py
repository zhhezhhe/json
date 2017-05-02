# coding: utf-8
import json
import simplejson
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('scenes.json', 'r') as f:
    data = json.load(f)
log_file = "sougou.log"
sougou_list = 'sougou_list.txt'
def search(query,data):
	pre1 = '_'
	pre2 = '-'
	af = ' '
	query2 = query.replace(pre1,af)
	query1 = query2.replace(pre2,af)
	for scene in data.keys():
		for keyword in data[scene]:
			if query1 in data[scene][keyword]:
				return scene
	return "not found"

# with open(log_file,'r') as reader, open('newfile.txt', 'w') as writer:
#     lines = reader.readlines()
#     size = len(lines)
#     print(size)
#     print(size/6)
#     for index in range(size):
#         if index % 6 == 0:
#         	# print(lines[index].split('\n')[0])
#             writer.write('\n')
#             writer.write(lines[index].split('\n')[0])
#         elif index % 6 == 1:
#         	query = lines[index].split('\n')[0].split(' ')[1]
#         	result = search(query,data)
#         	if(result !=  'not found'):
#         		# print(lines[index - 1].split('\n')[0])
#         		# print(result)
#         		writer.write(' ')
#         		writer.write(result)
#         		writer.write(' ')
#         elif index % 6 == 2:
#         	query = lines[index].split('\n')[0].split(' ')[1]
#         	result = search(query,data)
#         	if(result !=  'not found'):
#         		# print(lines[index - 1].split('\n')[0])
#         		# print(result)
#         		writer.write(' ')
#         		writer.write(result)
#         		writer.write(' ')
#         elif index % 6 == 3:
#         	query = lines[index].split('\n')[0].split(' ')[1]
#         	result = search(query,data)
#         	if(result !=  'not found'):
#         		# print(lines[index - 1].split('\n')[0])
#         		# print(result)
#         		writer.write(' ')
#         		writer.write(result)
#         		writer.write(' ')
#         elif index % 6 == 4:
#         	query = lines[index].split('\n')[0].split(' ')[1]
#         	result = search(query,data)
#         	if(result !=  'not found'):
#         		# print(lines[index - 1].split('\n')[0])
#         		# print(result)
#         		writer.write(' ')
#         		writer.write(result)
#         		writer.write(' ')
#         elif index % 6 == 5:
#         	query = lines[index].split('\n')[0].split(' ')[1]
#         	result = search(query,data)
#         	if(result !=  'not found'):
#         		# print(lines[index - 1].split('\n')[0])
#         		# print(result)
#         		writer.write(' ')
#         		writer.write(result)
#         		writer.write(' ')
  
# with open('newfile.txt','r') as reader, open(sougou_list, 'w') as writer:
#     lines = reader.readlines()
#     size = len(lines)
#     for line in lines:
#         # print(line.split('\n')[0])
#         # print(len(line.split('\n')[0].split(' ')) >= 2)
#         if(len(line.split('\n')[0].split(' ')) >= 2):
#         	# print(line.split('\n')[0].split(' ')[0])
#         	# print(line.split('\n')[0].split(' ')[1])
#         	writer.write(line.split('\n')[0].split(' ')[0])
#         	writer.write(' ')
#         	writer.write(line.split('\n')[0].split(' ')[1])
#         	writer.write('\n')
